Getting Started with UNIX
So what is UNIX anyways?  

Originally, Unix was meant to be a programmer's workbench to be used for developing software to be run on multiple platforms more than to be used to run application software. The system grew larger as the operating system started spreading in the academic circle, as users added their own tools to the system and shared them with colleagues.

Unix was designed to be portable, multi-tasking and multi-user in a time-sharing configuration. Unix systems are characterized by various concepts: the use of plain text for storing data; a hierarchical file system; treating devices and certain types of inter-process communication (IPC) as files; and the use of a large number of software tools, small programs that can be strung together through a command line interpreter using pipes, as opposed to using a single monolithic program that includes all of the same functionality. These concepts are collectively known as the "Unix philosophy." Brian Kernighan and Rob Pike summarize this in The Unix Programming Environment as "the idea that the power of a system comes more from the relationships among programs than from the programs themselves."

TLDR:
UNIX, unlike other systems, is ment to be modular, many small programs that do one thing well.  All the config files are plaintext and there is no registery (thank god) which means easy editing and customizing.

There are many "brands" of UNIX including Linux, FreeBSD, OS X, etc...  These are mostly sepreated by Kernels.  The kernel is a computer "program" that manages input/output requests from software, and translates them into data processing instructions for the central processing unit and other electronic components of a computer. The kernel is a fundamental part of a modern computer's operating system.  Linux is any UNIX system that uses the Linux kernel.  Android using the Linux kernel is most of their deployments and OS X used the FreeBSD kernal named Darwin.

When someone says "Do you know NIX?" what do they mean?
NIX is what many people call the family of UNIX and UNIX-like systems.  "Knowing" a system is more then just know the language of the system, it is also about knowing the software architecture of the system and why it works like it does.  We learn all of this in the framework of BASH.








Create an alias super easy, in this examle we create an alias 'subl' for opening Sublime Text 2. This assumes that you have sublime text 2 in your applications folder. (OSX)

```
$ echo "alias subl='/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl'" >> ~/.profile
source ~/.profile
```
