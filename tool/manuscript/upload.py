import os
import sys
import json
import subprocess
import readline


CONFIG_FILE = "tool/manuscript/config.json"
HTML_FILE = "tool/markdown2html/output/output.html"
POST_DATA = "tool/manuscript/data.json"
TO_HTML_CMD = ["", "-m", "tool.markdown2html.run_markdown2html"]
TO_HTML_CMD[0] = "python3" if sys.platform == "linux" else "python"
UPLOAD_CMD = ["/home/daniel/daniel/Google-api-python/bin/python3", "/home/daniel/daniel/Google-api-python/blogger/upload_post.py"]

def loadConfig ():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as config:
            return json.load(config)
    except:
        print("Init config...")
        defaultConfig = {}
        defaultConfig['blog'] = {"id": 4634073707460521498}
        with open (CONFIG_FILE, 'w+', encoding="utf-8") as config:
            json.dump(defaultConfig, config, ensure_ascii=False, indent=4)
            return defaultConfig

def saveConfig (config):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except:
        print("Warning: Save config failed.")

def transferToHTML (markdownFile):
    try:
        TO_HTML_CMD.append(markdownFile)
        subprocess.run(TO_HTML_CMD)
        with open (HTML_FILE, "r", encoding="utf-8") as html:
            return html.read() 
    except:
        print("Transfer to HTML failed.")
        quit()

def getPostData (config, html):
    retData = {}

    defaultStr = ""
    if "blog" in config:
        defaultStr = "(default: %s)" % (config["blog"]["id"])
    userTypeIn = input("Please enter the blod id%s:" % defaultStr)
    userTypeIn = userTypeIn.strip()
    retData['blog'] = {'id': userTypeIn if userTypeIn != "" or defaultStr == "" else config["blog"]["id"]}
    
    defaultStr = ""
    if "title" in config:
        defaultStr = "(default: %s)" % (config["title"])
    userTypeIn = input("Please enter the title%s:" % defaultStr)
    userTypeIn = userTypeIn.strip()
    retData['title'] = userTypeIn if userTypeIn != "" or defaultStr == "" else config["title"]

    defaultStr = ""
    if "labels" in config:
        defaultStr = "(default: %s)" % (str(config["labels"])[1:-1])
    userTypeIn = input("Please enter the labels%s:" % defaultStr)
    labels = []
    if userTypeIn != "":
        labels = userTypeIn.split(",")
        labels = [label.strip() for label in labels]
    retData['labels'] = labels if userTypeIn != "" or defaultStr == "" else config["labels"]

    saveConfig(retData)
    retData['content'] = html
    return retData

def savePostData (postData):
    try:
        with open (POST_DATA, "w+", encoding="utf-8") as f:
            json.dump(postData, f, indent=4, ensure_ascii=False)
    except:
        print("Save post data failed.")
        quit()

def uploadPost(postData):
    savePostData(postData)
    UPLOAD_CMD.append(POST_DATA)
    try:
        subprocess.run(UPLOAD_CMD)
        os.remove(POST_DATA)
    except:
        print("Upload failed.")
        os.remove(POST_DATA)
        quit()

def run ():
    
    # Quit process if there is no file path or file path is not valid.
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print("Error: Please enter the file path.")
        quit()

    # get file & config
    manuscriptFile = sys.argv[1]
    config = loadConfig()
    html = transferToHTML(manuscriptFile)
    
    # 
    uploadPost(getPostData(config, html))

if __name__ == "__main__":
    run()