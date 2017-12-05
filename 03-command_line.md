# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> >  
| command | what they do|
| -------- | ------------|
| pwd | show current working directory path|
|mkdir | creating a directory|
|rm -r <dir> | Remove a directory and contents|
|touch <file> | creating a file using `touch` command|
|rm <file> | deleting a file|
|mv <file name> <new file name>| renaming a file|
| ls -a | listing hidden files|
|cp <file path> <new file path> |copying a file from one directory to another|
|clear | clear screen|
|man [command]| show help for command|


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
|ls | Short listing|
|ls -a| Listing incl. hidden files|
|ls -l| Long listing|
|ls -lh|  Long listing with Human readable file sizes|
|ls -lah| Long listing with Human readable file sizes and hidden files|
|ls -t| Listing by time/date|
|ls -Glp| Long listing which doesn't show Group and has slash after each directory | 


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
|-r | Displays files in reverse order.|
|-R | Displays subdirectories as well.|
|-t | Displays newest files first. (based on timestamp)|
|-u|  Displays files by the file access time.|
|-x|  Displays files as rows across the screen.|

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs reads data from standard input (stdin) and executes the command (supplied to it as argument) one or more times based on the input read. Any blanks and spaces in input are treated as delimiters, while blank lines are ignored. An example would be 
```
$ find -name "*.txt" | xargs grep "abc"
```
>> where a txt file containing string "abc" is searched for

 

