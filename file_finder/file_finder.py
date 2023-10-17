import os
import mmap

def find_files_by_keyword(path, keywords,feature=0,caseSensitive=True):

    #Converts all keywords to lowercase if caseSensitive is False
    if not caseSensitive:
        for i in range(len(keywords)):
            keywords[i] = keywords[i].lower()
    
    filesfound = []
    filesbykeywords = {}

    #Initializes the filesbykewords dictionary with an empty list for each keyword
    for word in keywords:
        filesbykeywords.setdefault(word,[])

    #For each file, check if it contains the keywords.
    for root,dirs,files in os.walk(path):
        for afile in files:
            filepath = os.path.join(root,afile)
            with open(filepath,'r') as f:

                #mmap.mmap() method creates a bytearray object, and allows for faster I/O
                s = mmap.mmap(f.fileno(),0, access=mmap.ACCESS_READ)
                for kword in keywords:
                    if s.find(bytes(kword,'utf-8'))!= -1:
                        filesfound.append(afile)
                        print(f"Keyword '{kword}' found in the file '{afile}' at: {filepath}")
                        filesbykeywords[kword].append(afile)

    #Return as per requirement specified by feature parameter
    if len(filesfound)==0:
        print("No files found")
        return 0
    
    if feature==0:
        return filesfound
    elif feature == 1:
        return filesbykeywords

if __name__ == "__main__":
    thepath = "sample/path/tofiles"
    kwds = ["word1","word2"]
    print(find_files_by_keyword(thepath,kwds))

