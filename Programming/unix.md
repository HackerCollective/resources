Getting Started with UNIX
=========================

## <a name='toc'>Table of Contents</a>

  1. [An Introduction to UNIX](#intro)
  2. [Bash Tutorials](#tutorial)
  3. [The UNIX Philosophy](#laws)

## (#toc) <a name='intro'>So what is UNIX anyways?</a>

Originally, Unix was meant to be a programmer's workbench to be used for developing software to be run on multiple platforms more than to be used to run application software. The system grew larger as the operating system started spreading in the academic circle, as users added their own tools to the system and shared them with colleagues.

Unix was designed to be portable, multi-tasking and multi-user in a time-sharing configuration. Unix systems are characterized by various concepts: the use of plain text for storing data; a hierarchical file system; treating devices and certain types of inter-process communication (IPC) as files; and the use of a large number of software tools, small programs that can be strung together through a command line interpreter using pipes, as opposed to using a single monolithic program that includes all of the same functionality. These concepts are collectively known as the "Unix philosophy." Brian Kernighan and Rob Pike summarize this in The Unix Programming Environment as "the idea that the power of a system comes more from the relationships among programs than from the programs themselves."

####TLDR:
UNIX, unlike other systems, is meant to be modular, many small programs that do one thing well.  All the config files are plaintext and there is no registry (thank god) which means easy editing and customizing.

 http://en.wikipedia.org/wiki/Unix_philosophy#Eric_Raymond.E2.80.99s_17_Unix_Rules

There are many "brands" of UNIX including Linux, FreeBSD, OS X, etc...  These are mostly separated by Kernels.  The kernel is a computer "program" that manages input/output requests from software, and translates them into data processing instructions for the central processing unit and other electronic components of a computer. The kernel is a fundamental part of a modern computer's operating system.  Linux is any UNIX system that uses the Linux kernel.  Android using the Linux kernel is most of their deployments and OS X used the FreeBSD kernel named Darwin.

##When someone says "Do you know NIX?" what do they mean?

NIX is what many people call the family of UNIX and UNIX-like systems.  "Knowing" a system is more then just knowing the language of the system, it is also about knowing the software architecture of the system and why it works like it does.  We learn all of this in the framework of BASH.

##Why do I use it?
1. It is free as in freedom. (In price as well)

2. I can put my faith behind millions of coders and hackers on the internet rather than one company in the united states who can be manipulated by the government.

3. UNIX package managers are badass.

4. Incredibly hackable (in a good way).

5. Window managers and desktop environments options.

6. To be part of a powerful, very knowledgable community.

7. Just by learning linux I am on the path to being a sysadmin and eventually makes lots of money to make sure servers don’t' crash.  (Sounds like hell to some but sounds awesome to me)

8. I am addicted to distro hopping.

9. I hate windows, its registry, powershell, and its anti-UNIX philosophy.

10. Its Fun!

##Before we go any farther into NIX itself, lets get to know BASH.

Bash is a Unix shell written by Brian Fox for the GNU Project as a free software replacement for the Bourne shell (sh). Released in 1989, it has been distributed widely as the shell for the GNU operating system and as a default shell most NIX systems, including Linux and Mac OS X. 

The name itself is an acronym, a pun, and a description. As an acronym, it stands for Bourne-again shell, referring to its objective as a free replacement for the Bourne shell. As a pun, it expressed that objective in a phrase that sounds similar to born again, a term for spiritual rebirth. The name is also descriptive of what it did, bashing together the features of sh, csh, and ksh.

Terminal Time!
==============

You are encouraged to open up a terminal and follow along.  
<b>Learn though practice not memorization!</b>

####Navigation

Lets start with 3 basic but very important BASH commands: `ls`, `cd <path>`, and `pwd`.

Both `cd` and `ls` are fundamental in navigating the file structure of your system. 

`ls` lists all things in your current directory and cd, followed by a path, will take you into that directory.

If you need to know where you are just enter pwd to print your current working directory (The one you are in right now).

To go up one level in the file tree just enter `cd ..` .

The `~` character, called a tilde, is a default variable in most UNIX shells and it represents the users home directory.
To go home from anywhere, enter `cd ~` . On many systems the `cd` command with no path after it defaults to `cd ~` so the tilde is not always needed. I would recommend always using it as a beginner so that you get use to it, you will be using it in scripts later.  If you want to see what your home path is you can just `echo ~`.  

####Flags
In BASH there are also flags that ago along with commands.  These flag go after commands to adjust what the commands does and often effects it in very robust ways.  For example lets look at the command `ls` and then `ls -l`:

![](http://i.imgur.com/08vtwHH.png)

Above you can see I have executed two commands, both `ls`, but one with flag `l`.  `-l` stands for 'long' and it lists much more information than the regular `ls` including (from left to right): 

* files permissions, 
* number of links 
* owner's name
* owner's group
* file size
* time of last modification
* items name
 
####MAN PAGES!
RTFM is a common expression heard in this kind of field and it stands for READ THE F**KING MANUAL.  People in this community hate people who don't help themselves, they learned the hard way, why shouldn't you?  Its okay to ask questions but not stupid ones that could be easily googled.  To read the man page on any command just enter `man <command>` and then tap 'q' to the man page that is now open.

_____________________________________________________________________________


Create an alias super easy, in this example we create an alias 'subl' for opening Sublime Text 2. This assumes that you have sublime text 2 in your applications folder. (OS X)

```
$ echo "alias subl='/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl'" >> ~/.profile
source ~/.profile
```
