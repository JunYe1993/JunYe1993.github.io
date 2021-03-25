import os
import glob

def removeMarkdown ():
    for mdFile in glob.glob('article/[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md', recursive=True): 
        os.remove(mdFile)
        print(mdFile)

removeMarkdown()