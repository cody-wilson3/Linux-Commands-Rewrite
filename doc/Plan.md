# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* Write my own versions of the old Unix commands: cat, tac, cut, paste, grep, head, tail, sort, wc

**What a good solution looks like:**
* A good solution would be that the program crashes if given bad input by the user and the functions produce their intended output:
  * cat: concatenate files and prints their outputs
  * tac: concatenate files and print them in reverse
  * cut: remove sections from each line of files
  * paste: merge specified lines of files
  * grep: print lines of files matching a pattern
  * head: output the first lines of files specified by user
  * tail: output the last lines of files specified by user
  * sort: sort lines of text files
  * wc: print new line, word, and byte count for each file

**What I already know how to do:**
* I know how to open a file, read it, and close the file,
* I know how to use ASCII characters
* I know how to ask the user for information and give information back to them

**Foreseeable challenges:**
* I don't have ideas for the cut and paste functions right now.

## Phase 1: System Analysis *(10%)*

**Deliver:**

User Input:
  * The program they are running
  * The tool they are running with its optional option.
  * The filename they want to use the tool on

Output:
  * The output varies based on which tool is called for example if ```cat``` is called, then it concatenates the files and prints their outputs. see Phase 1.

Algorithms to be used:
  * A single function for each tool to bring out the expected output.
  
## Phase 2: Design *(30%)*

**Deliver:**

**cat**
```python
def cat(filename):
    variable =  open(filename)
    for line in variable.readlines():
        print(str(line))
```
**tac**
```python
def tac(argument):
    count = -1
    file = open(filename):
    for line in len(file.readlines()):
        print(file.readlines[count])    #realized that I can't evaluate this function at the count number
        count -= 1
```

**head**
```python
def head(args):
    if args[0] == "-n":
        if args[1].isnumeric():
            for i in (args[2:]):
                file = open(i)
                for i in range(int(args[1])):
                    for line in file.readlines():
                        print(line, end= '')
    else:
        for i in (args):
                file = open(i)
                for i in range(10):
                    for line in file.readlines():       #the readlines() function goes all the way through the file, I just want to
                        print(line, end= '')            #go one line at a time and print it out with the readline() function 
```

**wc**
```python
def wc(files):
    for i in files:
        file = open(files[i])
        readTheLines = file.readlines()
        numLines = len(readTheLines)
        for line in readTheLines:
            numWords = len(readTheLines.split())
        numBytes = len(file)
    
    print(numLines, numWords, numBytes)
```

**grep**
```python
def grep(args):
    if len(args) > 0:
        for i in range(len(args)):
            file = open(files[i])
            everyLine = file.readlines()
            for line in range(len(everyLine):
                if str(args[0]) in line:            #realized that "line" is not iterable so had to redo this whole thing
                    print(line)
```

**paste**
```python
def paste(args):
    if len(args) > 0:
        for i in range(len(args)):
            file = open(i)
            fileList = []
            fileList.append(file)
            everyLine = file.readlines()
            for j in fileList:
                for line in everyLine
                    print(line)
```
**cut**
```python
  list = []
    fileLengths = []                        #forgot that I have to check to see if there are enough arguments to run it and if not print errors
    if args[0] == "-f":
        for i in args[2:]:
            file = open(args[i])            #coaching center helped me recognize the difference between i as an element and as an index
            list.append(file)
        fileLength = len(file.readlines())
        listOfLines = file.readlines()
        targetColumn = int(args[1])
        for j in list:                      #forgot that I needed one section for the -f command and a separate section for the default command
            theLine = j.readline()
            splitLine = theLine.split(",")
            print(splitLine[args[1]])
```

**sort**
```python
def sort(args):
    fileList = []
    lineLengths = []
    firstCharList = []
    for i in range(len(args)):
        file = open(args[i])
        fileList.append(file)
    everyLineList = file.readlines()
    for line in everyLineList:
        lineLengths.append(len(line))
    maxlineLength = max(lineLengths)
    for i in everyLineList:
        firstCharList.append(ord(str(everLineList[i][0])))
    print(firstCharList)
        
        
        


```

## Phase 3: Implementation *(15%)*

**Deliver:**

**Learned:**
* For most of the assignment, I didn't know that "i" in a for loop can be used as an integer OR an element until one of the help lab people distinguished it. From this, debugging and writing was a lot easier.
* cut and paste are a lot easier in concept than writing them out.
* I wrote "cat" and "tac" separately, but after talking with some of my classmates, they just used a "reverse" operator on cat which would've saved me a lot of time but I don't know how to do that.

* **cat**
```python
def cat(filename):
    variable =  open(filename)
    for line in variable.readlines():
        print(str(line))
```

**tac**
```python
def tac(args):
    for i in args:                                  #realized that I have to treat the args as a list since there might be more than
        count = -1                                  #one argument passed into it.
        file = open[i]
        for line in range(len(file.readlines())):   #realized everytime if I call readlines() twice, then the second one won't do
            print(lineNumber)                       #anything because its at the end of the file. I have to seek() the beginning.
            count -= 1
```
**head**
```python
def head(args):
    if args[0] == "-n":
        if args[1].isnumeric():
            for i in (args[2:]):
                file = open(i)
                if len(args[1:]) > 2:
                    print("==>", i, "<==")
                    for i in range(int(args[1])):
                        lineText = file.readline()      #Had to open some files from DuckieCryptor to figure out how to use 
                        print(lineText, end='')         #the readline() function again
                    print("")
                else:
                    for i in range(int(args[1])):
                        lineText = file.readline()      #Originally didn't have this because I didn't read about printing the file
                        print(lineText, end='')         #name at the top but had to figure this out
                    file.close()
    else:
        for i in (args):
            file = open(i)
            file.seek(0)
            if len(args[0:]) > 1:
                print("==>", i, "<==")
                for i in range(10):
                    lineText = file.readline()
                    print(lineText, end='')
                print("")
            else:
                for i in range(10):
                    lineText = file.readline()
                    print(lineText, end='')
            file.close()
```
**wc**
```python
def wc(files):
    totalLines = 0
    totalWords = 0                                  #I tried to condense the code as much as possible in this function because my
    totalBytes = 0                                  #last functions were unnecessarily big even though they work
    for i in range(len(files)):                     #Used an overall for loop instead of multiple
        if len(files) > 0:
            file = open(files[i])
            everyLine = file.readlines()            #Named this so it would read more like English
            numLines = len(everyLine)
            numBytes = 0
            numWords = 0
            for string in everyLine:
                numBytes += len(string)             #lines 185-187 might be redundant and there's probably a simpler way, just 
                splitThis = str(string)             #couldn't think of it, and this works anyway so.
                numWords += len(splitThis.split())
            print(numLines, numWords, numBytes, files[i])
        totalLines += numLines
        totalWords += numWords
        totalBytes += numBytes
        print(totalLines, totalWords, totalBytes, "total")
```

**grep**
```python
def grep(args):
    if len(args) > 0:
        for i in (args[1:]):
            file = open(i)
            Lines = file.readlines()
            for j in range(len(Lines)):
                provString = args[0]
                if provString in Lines[j]:
                    print(Lines[j], end='')
```

**paste**
```python

list = []
    fileLengths = []
    for i in range(len(args)):          #for each file
        file = open(args[i])
        list.append(file)
    for k in range(len(args)):
        file2 = open(args[k])
        length = len(file2.readlines())
        fileLengths.append(length)
    maxLines = max(fileLengths)
    for line in range(int(maxLines)):                  #for this ammount of lines
        for j in list:                                                      #for each file
            print(j.readline().replace("\n", ""), end='')
            if len(j.readlines()) != j:
                print(",", end="")
        print(" ")
```

**cut**
```python
def cut(args):
    list = []
    fileLengths = []
    if args:
        if args[0] == "-f":
            if len(args[1:]) >0:
                var = args[1].split(",")
                var.sort()
                for i in args[2:]:
                    file = open(i)
                    list.append(file)
                for j in list:
                    for line in j.readlines():
                        for k in var:
                            splitLine = line.split(",")
                            if int(k) <= len(splitLine):
                                if k == var[len(var)-1]:
                                    print(splitLine[int(k) - 1].strip())
                                else:
                                    print(splitLine[int(k) - 1].strip(), end=',')
                            else:
                                print("")
                    j.close()
            else:
                usage("A comma-separated field specification is required", "cut")
        else:
            for i in range(len(args)):
                file = open(args[i])
                list.append(file)
            for k in range(len(args)):
                file2 = open(args[k])
                length = len(file2.readlines())
                fileLengths.append(length)
            maxLines = max(fileLengths)
            for line in range(maxLines):
                for j in list:
                    theLine = j.readline()
                    splitLine = theLine.split(",")
                    print(splitLine[0])
            for j in list:
                j.close()

    else:
        usage("Too few arguments", "cut")
```

**sort**
```python
fileList = []
    masterList = []
    if args:
        for i in range(len(args)):      #Finally figured out how to use for loops properly by knowing the difference between i as an element and i as a index
            file = open(args[i])
            fileList.append(file)
        for j in fileList:
            sentList = j.readlines()
            for k in sentList:
                masterList.append(k)
        sortedList = sorted(masterList)     #For some reason, I can't figure out how to invoke help() on the sort() function in the REPL
        for i in range(len(sortedList)):
            print(sortedList[i], end='')
    else:
        usage("Too Few Arguments", "sort")
```

## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

**Tested:**
* I was constantly testing with the code provided in the "examples" folder, copying and pasting that information to Git Bash to see if the output matched what it should.
* My main problem that I was running into was I was confused on the "i" in the for loop as an index or an element in the list. Testing didn't really show the difference.
* My testing strategy was to build the function with the "optional" argument first, then just do an "else" statement for the alternate half. If I did it again, I would do it the other way around.

## Phase 5: Deployment *(5%)*

**Deliver:**

**Deployed?**
* Pushed to Gitlab, test cases work, eyes bloodshot, sleep lost, everyone happy.


## Phase 6: Maintenance

**Deliver:**

* Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    * What parts of your program are sloppily written and hard to understand?
      * I think my cut and paste functions are suspiciously long. They work, and I'm sure if I spent more time staring at the screen with all the new knowledge I have I could condense them.
    * Are there parts of your program which you aren't quite sure how/why they work?
      * NO! - Through a painful process I now can explain everything in immense detail after the hours sunk into this project.
    * If a bug is reported in a few months, how long would it take you to find the cause?
      * Most likely less than 5 minutes. I named things pretty well so I think it would be easy to find.
    * Will your documentation make sense to...
        * ...anybody besides yourself?
          * probably, the naming conventions and layout are pretty intuitive.
        * ...yourself in six month's time?
          * for sure! I wrote it so I think the layout would make sense to me then still.
    * How easy will it be to add a new feature to this program in a year?
      * depends on the feature.
    * Will your program continue to work after upgrading...
        * ...your computer's hardware?
          * Don't know enough after upgrading.
        * ...the operating system?
          * I don't think updating the operating system changes python so yes.
        * ...to the next version of Python?
          * depends on what is changed.
    * Fill out the Assignment Reflection on Canvas.
      * you got it Michael Scott
