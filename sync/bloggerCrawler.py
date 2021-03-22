import requests
from bs4 import BeautifulSoup
import sync.bloggerSync as sync

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
    post['config']['title'] = soup.find('title').string
    post['config']['author'] = soup.find('a', {'rel': 'author'}).span.string
    post['config']['published'] = soup.find('span', {'class': 'byline post-timestamp'}).a.time['datetime']
    post['config']['tag'] = []
    for tag in soup.find_all('a', {'rel': 'tag'}):
        post['config']['tag'].append(tag.string)

    # return prettify data string
    soup = BeautifulSoup(str(post['content']), features="lxml")
    post['content'] = str(soup.prettify()) 
    return post

def blogger_sitemap_spider (url):
    data = {}
    data['post'] = []
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for title in soup.find_all('loc'):
        if title != None:
            data['post'].append(title.string[30:])

    return data

if __name__ == "__main__":

    # Get blogger sitemap and local sitemap
    sitemap_url = 'http://junye1993.blogspot.com/sitemap.xml'
    blogger_article_map = blogger_sitemap_spider(sitemap_url)
    local_article_map = sync.getArticleMap()

    # Compare two sitemaps, see if there is new post.
    new_posts = []
    local_posts = set(local_article_map['post'])
    for post in blogger_article_map['post']:
        if post not in local_posts:
            new_posts.append(post)

    # get new post
    count = 0
    for post in new_posts:
        # get post
        url = 'http://junye1993.blogspot.com/' + post
        data = blogger_article_spider(url)

        # save post
        sync.saveArticleContent("./article/"+post, data['content'])
        sync.saveArticleConfig("./article/"+post, data['config'])
        sync.saveSiteMap(local_article_map, post)
        
        count+=1
        print("Progress: "+str(count)+"/"+str(len(new_posts)))


