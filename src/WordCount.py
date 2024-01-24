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
def wc(files):
    totalLines = 0
    totalWords = 0
    totalBytes = 0
    if len(files) > 0:
        for i in range(len(files)):
            if len(files) > 0:
                file = open(files[i])
                everyLine = file.readlines()
                numLines = len(everyLine)
                numBytes = 0
                numWords = 0
                for string in everyLine:
                    numBytes += len(string)
                    splitThis = str(string)
                    numWords += len(splitThis.split())
                print(format(numLines, "<6"), format(numWords, "<6"), format(numBytes, "<6"), format(files[i], "<6"))
            totalLines += numLines
            totalWords += numWords
            totalBytes += numBytes
            print(format(totalLines, "<6"), format(totalWords, "<6"), format(totalBytes, "<6"), "total")
            file.close()
    else:
        usage("Too Few Filenames Provided", "wc")
