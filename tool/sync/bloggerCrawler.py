import re
import requests
from bs4 import BeautifulSoup

def blogger_article_spider (url):
    post = {}
    post['config'] = {}

    # get source code
    source_code = requests.get(url)
    plain_text = source_code.text
    # get target tag and its contents
    soup = BeautifulSoup(plain_text, features="lxml")
    post['content'] = soup.find('div', {'class': 'post-body entry-content float-container'})
    post['config']['url'] = url
    post['config']['title'] = soup.find('h2', {'class': 'post-title entry-title'}).a.string
    post['config']['author'] = "JunYe" # no longer accessible from html
    post['config']['published'] = soup.find('span', {'class': 'nbtpost-date'}).string
    post['config']['tag'] = []
    for tag in soup.find_all('span', {'class': 'nbttags-links'}):
        post['config']['tag'].append(tag.a.string)

    # return prettify data string
    soup = BeautifulSoup(str(post['content']), features="lxml")
    post['content'] = str(soup.prettify()) 
    return post

def blogger_sitemap_spider (url):
    data = {'post': []}
    pattern = r'sitemap.xml\?page=[1-9]+'
    print(url)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for title in soup.find_all('loc'):
        if title != None:
            if re.search(pattern, title.string):
                pagePost = blogger_sitemap_spider(title.string)['post']
                data['post'] += pagePost
            else:
                data['post'].append(title.string[30:])

    return data




