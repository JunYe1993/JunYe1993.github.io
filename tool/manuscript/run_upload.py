import os
import sys
import json
import subprocess

import tool.markdown2html.run_markdown2html as m2html
import tool.sync.run_sync as sync

CONFIG_FILE = "tool/manuscript/config.json"
HTML_FILE   = "tool/markdown2html/output/output.html"
POST_DATA   = "tool/manuscript/data.json"
ENV_PATH    = "/home/daniel/daniel/Google-api-python"
UPLOAD_CMD  = [ENV_PATH+"/bin/python3", ENV_PATH+"/blogger/upload_post.py"]

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
        with open (markdownFile, "r", encoding="utf-8") as md:
            return m2html.transMDtoHTML(md.read())
    except:
        print("Transfer failed.")
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

def savePostData (postData, dataPath):
    try:
        with open (dataPath, "w+", encoding="utf-8") as f:
            json.dump(postData, f, indent=4, ensure_ascii=False)
    except:
        print("Save post data failed.")
        quit()

def uploadPost(postData, dataPath):
    # get platform setting
    getPlatformCommand()
    savePostData(postData, dataPath)
    UPLOAD_CMD.append(dataPath)
    try:
        process = subprocess.run(UPLOAD_CMD, stdout=subprocess.PIPE)
    except:
        print("Upload failed.")
        os.remove(dataPath)
        quit()

    os.remove(dataPath)
    return process.stdout.decode("ascii")

def run_upload (manuscriptFile):
    # get file & config
    config = loadConfig()
    html = transferToHTML(manuscriptFile)
    
    # upload & return post id
    return uploadPost(getPostData(config, html), os.path.abspath(POST_DATA))

# for my windows
def getPlatformCommand ():
    global ENV_PATH
    if sys.platform == "win32":
        ENV_PATH = "C:\\Users\\10903029\\Desktop\\my\\google.python.api"
        UPLOAD_CMD[0] = ENV_PATH + "\\Scripts\\python.exe"
        UPLOAD_CMD[1] = ENV_PATH + "\\blogger\\upload_post.py"

def run_sync (file=None):
    try:
        sync.run(file)
    except:
        print("Sync failed.")
        quit()

def run (manuscriptFile):
    # update to last by sync once
    #run_sync()
    run_upload(manuscriptFile)
    #run_sync(manuscriptFile)

if __name__ == "__main__":
    # Quit process if there is no file path or file path is not valid.
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        print("Error: Please enter the file path.")
        quit()
    run(sys.argv[1])
