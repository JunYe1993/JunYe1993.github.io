import os
import sys
import markdown
import tool.markdown2html.html2myblogstyle as h2myhtml

def checkArg1Valid () -> bool:
    if len(sys.argv) == 1:
        print("Please input the file name.")
        quit()
    else:
        return os.path.isfile(sys.argv[1])

def transMDtoHTML (content, option = None):
    html = markdown.markdown(content, extensions=['fenced_code'])
    with open ("./tool/markdown2html/output/output.html", "w+", encoding="utf-8") as f:
        html = h2myhtml.myBloggerPrettify(html, option)
        f.write(html)
    return html

def run (option = None):
    # check if $1 is valid file.
    if not checkArg1Valid():
        print("Please the valid file name.")
        quit()

    # get file data
    targetFile = sys.argv[1]
    with open (targetFile, "r", encoding="utf-8") as sourcefile:
        targetData = sourcefile.read()
        transMDtoHTML(targetData, option)

if __name__ == "__main__":
    option = None if len(sys.argv) < 3 else sys.argv[2]
    run(option)
    
