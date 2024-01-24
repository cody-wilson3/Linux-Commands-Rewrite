#                         ~                                         	         	  
#                        (o)<  DuckieCorp Software License          	         	  
#                   .____//                                         	         	  
#                    \ <' )   Copyright (c) 2022 Erik Falor         	         	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	  
#                                                                   	         	  
# Permission is NOT granted, to any person who is NEITHER an employee NOR     	  
# customer of DuckieCorp, to deal in the Software without restriction,        	  
# including without limitation the rights to use, copy, modify, merge,        	  
# publish, distribute, sublicense, and/or sell copies of the Software, and to 	  
# permit persons to whom the Software is furnished to do so, subject to the   	  
# following conditions:                                             	         	  
#                                                                   	         	  
# The above copyright notice and this permission notice shall be included in  	  
# all copies or substantial portions of the Software.               	         	  
#                                                                   	         	  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  	  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,    	  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 	  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER      	  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING     	  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS	  
# IN THE SOFTWARE.                                                  	         	  

from Usage import usage
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



def paste(args):
    list = []
    fileLengths = []
    if args:
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
                if list[len(list)-1] != j:
                    print(",", end="")
            print(" ")
    else:
        usage("Too Few Arguments", "paste")






