import os
import sys
import json
import subprocess

CONFIG_FILE = "tool/manuscript/config.json"
HTML_FILE = "tool/markdown2html/output/output.html"
POST_DATA = "tool/manuscript/data.json"
TO_HTML_CMD = ["python3", "-m", "tool.markdown2html.run_markdown2html"]
ENV_PATH = "/home/daniel/daniel/Google-api-python"
UPLOAD_CMD = [ENV_PATH+"/bin/python3", ENV_PATH+"/blogger/upload_post.py", ENV_PATH]
SYNC_CMD = ["python3", "-m", "tool.sync.run_sync"]

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

def run_upload (manuscriptFile):
    # get file & config
    config = loadConfig()
    html = transferToHTML(manuscriptFile)
    
    # upload
    uploadPost(getPostData(config, html))

# for my windows
def getPlatformCommand ():
    global ENV_PATH
    if sys.platform == "win32":
        ENV_PATH = "C:\\Users\\10903029\\Desktop\\my\\google.python.api"
        UPLOAD_CMD[0] = ENV_PATH + "\\Scripts\\python.exe"
        UPLOAD_CMD[1] = ENV_PATH + "\\blogger\\upload_post.py"
        UPLOAD_CMD[2] = ENV_PATH
        TO_HTML_CMD[0] = "python"
        SYNC_CMD[0] = "python"

def run_sync (file=None):
    if file:
        SYNC_CMD.append(file)
    try:
        subprocess.run(SYNC_CMD)
    except:
        print("Sync failed.")
        quit()

if __name__ == "__main__":
    # Quit process if there is no file path or file path is not valid.
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print("Error: Please enter the file path.")
        quit()
    manuscriptFile = sys.argv[1]

    # get platform setting
    getPlatformCommand()

    # update to last by sync once
    run_sync()
    run_upload(manuscriptFile)
    run_sync(manuscriptFile)
