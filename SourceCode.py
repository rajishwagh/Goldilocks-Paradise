'''
Created on Jun 19, 2017

@author: rjw0028
'''
import os, io, re, FileDialog
import matplotlib.pyplot as plt


#root_dir="C:\\Users\\rjw0028\\Desktop\\TestFolder"

print ''' 
This program tries to solve the following problem.
_____________________________________________________________
 
Use Python.
Implement a stand-alone script that does the following function:
Takes an argument root_dir... This will be a path in string format...
Also, takes an argument called keyword... This is also a string which 
contains a phrase.

The phrase can look like this, "^[a-zA-Z]+_TESTResult.*" and several files 
in the root directory as well as sub directories, contain this phrase.
 
The programmer\s job is to go through the root directory look at all the 
files to detect those which contain this phrase. The number of such files 
in each sub directory is to be counted and represented in the output format given.
_____________________________________________________________

Here are a few scenarios this, code will not work: 

1. If the keyword entered does not follow the rules of regular expressions 
in Python 2.7 documentation. (https://docs.python.org/2/library/re.html)

2. If the files included in the directories are not 'plaintext' files. 
I tried to fix the encoding issues, however, complex file systems like .docx 
are actually compressed file systems and couldn't figure out a way around that.

'''


def functocheckmatch(filename, dirnam):
    fullpath = os.path.join(dirnam,filename)
    with io.open(fullpath, 'r', encoding = 'utf-8') as fil:
        text = fil.read()
        
    if re.search(pattern, text, flags=0):
        return True
    else:
        return False

def main():
    global root_dir
    print "Enter path for the root directory: (for example: 'C:\\Users\\rjw0028\\Desktop\\TestFolder')"
    root_dir = raw_input()
    global AllDirs
    AllDirs = [root_dir]
    
    print "Enter the keyword as a valid regular expression: (for example: '\d+[a-zA-Z]*') "
    keyword = raw_input()
    global pattern
    pattern = re.compile(keyword, re.I|re.M)

    global OutputArrayDict
    OutputArrayDict = {}
    for i in AllDirs:
        for item in os.listdir(i):
            fullpath = os.path.join(i,item)
            if os.path.isdir(fullpath):
                AllDirs.append(fullpath)
 
    for f in AllDirs:
        files = next(os.walk(f))[2]
        count = 0
        for j in files:         # j is each file
            if functocheckmatch(j, f):
                count += 1
        OutputArrayDict[f] = count
    
    
    keylist = OutputArrayDict.keys()
    keylist.sort()
    
    for key in keylist:
        print key, "    :    ", OutputArrayDict[key]
        
    
    plt.plot(range(len(OutputArrayDict.keys())), OutputArrayDict.values(), 'ro')
    plt.axis([-1, len(OutputArrayDict.keys()) , -1, max(OutputArrayDict.values())+1])
    plt.show()
    raw_input()
    

if __name__ == "__main__":
    main()
