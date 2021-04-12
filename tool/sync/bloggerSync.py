import os
import glob
import json

local_article_map = "tool/sync/articleMap.json"

def existArticleScan ():
    local_data = {}
    local_data['post'] = []
    for pathName in glob.glob('article/[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.html', recursive=True): 
        pathName = pathName.replace('\\', '/')  # windows might return **\**\* instead of **/**/*
        pathName = pathName[8:]  # get rid of "article/"
        local_data['post'].append(pathName)
    local_data['post'].sort()
    return local_data

def getArticleMap ():
    local_data = {}
    try: 
        with open (local_article_map) as json_file:
            local_data = json.load(json_file)
    except:
        print("Local Article Map is empty.")
        print("Scanning Article that exists...")
        local_data = existArticleScan()
        with open (local_article_map, 'w+') as json_file:
            json.dump(local_data, json_file, ensure_ascii=False, indent=4)

    return local_data

def createDir (fileName):
    def recursiveCreateDir (filePath):
        filePath = os.path.dirname(filePath)
        if not os.path.isdir(filePath):
            try:
                os.mkdir(filePath)
            except:
                recursiveCreateDir(filePath)
                os.mkdir(filePath)
    recursiveCreateDir(fileName)

def saveArticleContent (fileName, content):
    # create dir if it needs.
    createDir(fileName)
    
    # write post data to local file.
    with open (fileName, "w+", encoding="utf-8") as f:
        f.write(content)

def saveArticleConfig (fileName, config):
    # create dir if it needs.
    path = createDir(fileName)

    # write post data to local file.
    with open (fileName[:-5] + ".json", "w+", encoding="utf-8") as json_file:
        json.dump(config, json_file, ensure_ascii=False, indent=4)

def saveSiteMap (localSiteMap, newAtrticle):
    localSiteMap['post'].append(newAtrticle)
    localSiteMap['post'].sort()
    with open (local_article_map, "w+", encoding="utf-8") as json_file:
        json.dump(localSiteMap, json_file, ensure_ascii=False, indent=4, sort_keys=True)

def saveMarkDownFile (post, fileName):
    # create dir if it needs.
    path = createDir(fileName)

    with open (fileName, "r", encoding="utf-8") as src:
        with open (post[:-5] + ".md", "w+", encoding="utf-8") as md_file:
            md_file.write(src.read())

if __name__ == "__main__":
    createDir("tool/article/123/asdad/regeg")