import json
import glob

local_html_map = "tool/html2markdown/htmlMap.json"
local_markdown_map = "tool/html2markdown/markdownMap.json"

def existHtmlScan ():
    local_data = {}
    local_data['post'] = []
    for pathName in glob.glob('article/[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.html', recursive=True): 
        pathName = pathName.replace('\\', '/')  # windows might return **\**\* instead of **/**/*
        pathName = pathName[8:]  # get rid of "article/"
        pathName = pathName[:-5] # get rid of ".html"
        local_data['post'].append(pathName)
    local_data['post'].sort()
    return local_data

def getHtmlMap ():
    local_data = {}
    try: 
        with open (local_html_map) as json_file:
            local_data = json.load(json_file)
    except:
        print("Local Article Map is empty.")
        print("Scanning Article that exists...")
        local_data = existHtmlScan()
        with open (local_html_map, 'w+') as json_file:
            json.dump(local_data, json_file, ensure_ascii=False, indent=4)

    return local_data

def existMarkdownScan ():
    local_data = {}
    local_data['post'] = []
    for pathName in glob.glob('article/[0-9][0-9][0-9][0-9]/[0-9][0-9]/*.md', recursive=True): 
        pathName = pathName.replace('\\', '/')  # windows might return **\**\* instead of **/**/*
        pathName = pathName[8:]  # get rid of "article/"
        pathName = pathName[:-3] # get rid of ".md"
        local_data['post'].append(pathName)
    local_data['post'].sort()
    return local_data

def getMarkdownMap ():
    local_data = {}
    try: 
        with open (local_markdown_map) as json_file:
            local_data = json.load(json_file)
    except:
        print("Local Article Map is empty.")
        print("Scanning Article that exists...")
        local_data = existMarkdownScan()
        with open (local_markdown_map, 'w+') as json_file:
            json.dump(local_data, json_file, ensure_ascii=False, indent=4)

    return local_data

def saveMarkdownMap (localSiteMap, newAtrticle):
    localSiteMap['post'].append(newAtrticle)
    localSiteMap['post'].sort()
    with open (local_markdown_map, "w+", encoding="utf-8") as json_file:
        json.dump(localSiteMap, json_file, ensure_ascii=False, indent=4, sort_keys=True)