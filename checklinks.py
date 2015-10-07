#!/usr/bin/env python2
from __future__ import print_function

import threading
import Queue

import StringIO

# determine the best number of threads to run with
import multiprocessing

# needed to print to sys.stderr
import sys

# so we can get the output of `git grep ...`
import subprocess

# sanitise links so we don't get issues with checking URLs with spaces in them
import urllib

# NOTE: will require the `pycurl` package: `pip install pycurl`
import pycurl

# so we don't have to pipe to `sed`. used over `re` so we have slightly more
# powerful regexes, as per http://stackoverflow.com/a/25109573
# NOTE: will require the `regex` package: `pip install regex`
import regex

# may as well have nicely formatted output
# NOTE: will require the `termcolor` package: `pip install termcolor`
from termcolor import colored


# Adapted from http://stackoverflow.com/a/25109573; why hand write our own,
# less efficient regex?
# replace the `\S` with `[^\r\n\t\f )]` so we don't match the badge URLs
URL_REGEX = '(?|(?<txt>(?<url>(?:ht|f)tps?://[^\r\n\t\f )]+(?<=\P{P})))' + \
            '|\(([^)]+)\)\[(\g<url>)\])'

NUM_WORKER_THREADS = multiprocessing.cpu_count() * 2
# do we want to follow redirects from websites?
FOLLOW_REDIRECTS = 1
# spoof our UA to be Chrome so we don't get false positives from sites who
# don't like webscraping. UA taken from
# http://www.useragentstring.com/Chrome41.0.2228.0_id_19841.php
USERAGENT = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like " + \
            "Gecko) Chrome/41.0.2228.0 Safari/537.36"
# limit the time we're just sitting around waiting for the script to run by
# default, it's running at 300 seconds, which is a bit painful to wait for
TIMEOUT = 30

# global Queue object to manage our URLs to crawl
gQueue = Queue.Queue()
# global dict to hold [file]->[[URLs to be changed]]
gProcessed = dict()
# use a lock to ensure that we can't overwrite our dict, or global error flag,
# by multiple threads accessing it at once
gProcessedLock = threading.Lock()

# a flag we can use to determine whether we've found any errors, be they an
# exception, or just a normal site error
gEncounteredErrors = False


# Nicely formatted error messages are always better than ones that merge in
# with the rest of them, and that we can't distinguish. We also get them to
# stderr, which is way better.
def error(errorMessage):
    """
    Produce a red-coloured error message to stderr.

    Format our messages so they're much more readily distinguishable from
    normal output. Also write them to stderr so if we're piping output we
    get them on the right stream.
    """
    print(colored(errorMessage, 'red'), file=sys.stderr)


def getStatusCode(url):
    """Given a URL, get the status code when trying to access it"""

    # escape the URL so we don't get 404s on URLs with spaces in them
    url = urllib.quote(url, safe=':&?/=#-+')

    curl = pycurl.Curl()
    buff = StringIO.StringIO()

    curl.setopt(pycurl.URL, url)
    # make sure we don't dump the page content to stdout
    curl.setopt(pycurl.WRITEFUNCTION, buff.write)
    curl.setopt(pycurl.FOLLOWLOCATION, FOLLOW_REDIRECTS)
    curl.setopt(pycurl.USERAGENT, USERAGENT)
    curl.setopt(pycurl.CONNECTTIMEOUT, TIMEOUT)

    try:
        curl.perform()
    except pycurl.error as pycurl_error:
        error("Received pycurl error %s while processing %s" % (
              pycurl_error,
              url)
              )

        # not being able to access the host is basically a 404
        if pycurl_error.args[0] == pycurl.E_COULDNT_RESOLVE_HOST:
            return 404
        else:
            # if we haven't got a default case, still throw our error
            raise pycurl_error

    return int(curl.getinfo(pycurl.HTTP_CODE))


# a central way to update our dict of files with the broken URLs
def addToDict(url, matchedFiles):
    """
    Retain a URL and any files it appears in.

    Store inside our global dictionary files and URLs that appear in them that
    need to be fixed. Thread-safe.
    """

    with gProcessedLock:
        global gEncounteredErrors
        gEncounteredErrors = True
        for matchedFile in matchedFiles:
            if matchedFile not in gProcessed:
                gProcessed[matchedFile] = []

            # stop us getting duplicates
            if url not in gProcessed[matchedFile]:
                gProcessed[matchedFile].append(url)


def worker():
    """Worker for Threads to process URLs"""

    # always be ready to take a new job
    while True:
        # default an empty string, so if we hit the generic catch, we don't
        # have an unset variable
        url = ""
        try:
            url = gQueue.get()
            statusCode = getStatusCode(url)
            didValidate = (statusCode < 400 or statusCode >= 500)
            if not didValidate:
                # work out what files are affected by the broken URL
                filesWithUrl = subprocess.check_output(["git", "grep", "-l",
                                                        url])
                addToDict(url, filesWithUrl.splitlines())
            gQueue.task_done()
        except:
            with gProcessedLock:
                global gEncounteredErrors
                gEncounteredErrors = True

            error("An exception occured while processing %s" % url)
            # make sure we mark our task as done, otherwise our threads
            # will just hang
            gQueue.task_done()
        gQueue.task_done()


def main():
    gitGrep = subprocess.Popen(["git", "grep", "(\s*http.*)"],
                               stdout=subprocess.PIPE)
    for line in gitGrep.stdout:
        urls = regex.findall(URL_REGEX, line)
        for url in urls:
            gQueue.put(url[1])

    for i in range(NUM_WORKER_THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()

    # block until we've finished all our jobs
    gQueue.join()

    # finally output each file and the corresponding URLs to fix/remove
    for key in gProcessed:
        print("%s has the following changes needed:" % (
              colored(key, 'yellow')))

        for url in gProcessed[key]:
            print("- %s" % url)

    # an empty dict evaluates as False, so we can take advantage of that to
    # return 0 when we have no matches, and 1 when there are matches
    sys.exit(gEncounteredErrors)


if __name__ == "__main__":
    main()
