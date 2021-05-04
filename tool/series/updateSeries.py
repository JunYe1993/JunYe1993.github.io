import os
import sys
import json
import requests
import tool.markdown2html.run_markdown2html as m2html
import tool.sync.bloggerCrawler as crawler
import tool.manuscript.run_upload as upload

TEMP_DATA = "tool/series/data.json"

def loadConfig (file):
    with open (file, 'r', encoding='utf-8') as f:
        config = json.load(f)
        return config

def saveConfig (file, config):
    with open (file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

def writeMarkdown (config):
    content = ""
    for subTitle in config['sub-titles']:
        content += markdown_Head(subTitle['title'])
        for post in subTitle['posts']:
            content += markdown_Href(post)
    return content

def markdown_Head (string) -> str:
    return '## %s ##\n\n' % (string)

def markdown_Href (post) -> str:
    href = "https://junye1993.blogspot.com/" + post
    title = crawler.blogger_article_spider(href)['config']['title']
    return '- **<a href=%s>%s</a>**\n\n' % (href, title)

def getConfig (html, config):
    data = config['config']
    data['content'] = html
    return data

def run ():
    config = None
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            config = loadConfig(sys.argv[1])
    
    if not config:
        print("Error: config failed")
        quit()
    else:
        markdown = writeMarkdown(config)
        html = m2html.transMDtoHTML(markdown)
        postid = upload.uploadPost(getConfig(html, config), TEMP_DATA)
        
        config['config']['id'] = postid
        saveConfig(sys.argv[1], config)

if __name__ == "__main__":
    run ()
        