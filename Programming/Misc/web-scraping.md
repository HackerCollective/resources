Web Scraping
===============================

## Intro
Web Scraping is some crazy shit that allows you can use for many reasons.  A good way to use it is to create your own version of an API, or if a site/serice doesn't supply a good enough API of their own.  

## <a name='toc'>Table of Contents</a>

  1. [Resources](#resources)
  2. [Parsers](#parsers)
  3. [Robots.txt](#robots)


### [[⬆]](#toc) <a name='resources'>Scraping Libraries:</a>
1. Python
    1. [Urllib](https://docs.python.org/2/library/urllib.html) | This is a stdlib option and definitely not suggested!
    2. [Requests](http://docs.python-requests.org/en/latest/) | By far the best option available.
    3. [Scrapy](http://scrapy.org/)
2. Node.js (Javascript)
    1. [Requestjs](https://github.com/mikeal/request)
3. Ruby
4. Java



### [[⬆]](#toc) <a name='parsers'>Parsers:</a>
1. Python
    1. [BeautifulSoup](http://beautiful-soup-4.readthedocs.org/en/latest/) | Community accepted best Python tool for parsing HTML/XML
2. Node.js (JavaScript)
    1. [Cheerio](https://github.com/cheeriojs/cheerio) | Server sided jQuery tool that allows you to manipulate scraped pages with jQuery like features (has other uses too!)
3. Ruby
4. Java

### [[⬆]](#toc) <a name='robots':>Robots.txt:</a>
The Robots.txt is a publically viewable file that most (any site worth it's weight) will have.  It tells a viewer/robot which type of robots/crawlers are allowed and to which parts of the site.  Example:
```
User-Agent: *
Disallow: /
```
This script would tell all user's `*` that they cannot crawl any part of the site `/`.  But if you were to check out GitHub's [Robot.txt](https://github.com/robots.txt) you would see that they allow specific bots, and disallow ones that they are not aware of.  Many websites will be like this.  But as a writer of a web crawler you have the ability to not follow these guidlines, just like it isn't necessary to color between the lines of a coloring book.  The author will probably never know (unless your crawler is doing an extensive amount of traffic/ malicious things), but you will.   
