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


def head(args):
    errorMessage = "Error: Number of Lines is Required\n\n tt.py head|tail [-n N] FILENAME...\n\t Output the first or last part of files\n\t -n  Number of lines to print (default is 10)"
    if len(args) > 0:
        if args[0] == "-n" or args[0] == "N":
            if len(args[1:]) >0:
                if args[1].isnumeric():
                    for i in (args[2:]):
                        file = open(i)
                        if len(args[1:]) > 2:
                            print("==>", i, "<==")
                            for i in range(int(args[1])):
                                lineText = file.readline()
                                print(lineText, end='')
                            print("")
                        else:
                            for i in range(int(args[1])):
                                lineText = file.readline()
                                print(lineText, end='')
                            file.close()
                else:
                    print(errorMessage)
            else:
                print(errorMessage)
        else:
            for i in (args):
                file = open(i)
                file.seek(0)
                if len(args[0:]) > 1:
                    print("==>", i, "<==")
                    for j in range(10):
                        lineText = file.readline()
                        print(lineText, end='')
                    print("")
                else:
                    for j in range(10):
                        lineText = file.readline()
                        print(lineText, end='')
                file.close()
    else:
        print("Error: Too Few Arguments")





def tail(args):
    errorMessage = "Error: Number of Lines is Required\n\n tt.py head|tail [-n N] FILENAME...\n\t Output the first or last part of files\n\t -n  Number of lines to print (default is 10)"
    if len(args) > 0:
        if args[0] == "-n" or args[0] == "N":
            if len(args[1:]) > 0:
                if args[1].isnumeric():
                    for i in (args[2:]):
                        file = open(i)
                        lineText = file.readlines()
                        lenOfFile = (len(lineText)- int(args[1]))
                        if len(args[1:]) > 2:
                            print("\n==>", i, "<==")
                        for j in range(lenOfFile, len(lineText)):
                            print(lineText[j], end='')
                        file.close()
                else:
                    print(errorMessage)
            else:
                print(errorMessage)
        else:
            for i in (args):
                file = open(i)
                file.seek(0)
                lineText = file.readlines()
                if len(args[0:]) > 1:
                    print("\n==>", i, "<==")

                for j in range(len(lineText) - 10, len(lineText)):
                    print(lineText[j], end='')
                file.close()
    else:
        print("Error: Too Few Arguments")
