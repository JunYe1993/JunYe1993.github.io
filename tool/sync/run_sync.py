import tool.sync.bloggerSync as sync
import tool.sync.bloggerCrawler as crawler

if __name__ == "__main__":

    # Get blogger sitemap and local sitemap
    sitemap_url = 'http://junye1993.blogspot.com/sitemap.xml'
    blogger_article_map = crawler.blogger_sitemap_spider(sitemap_url)
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
        data = crawler.blogger_article_spider(url)

        # save post
        sync.saveArticleContent("./article/"+post, data['content'])
        sync.saveArticleConfig("./article/"+post, data['config'])
        sync.saveSiteMap(local_article_map, post)
        
        count+=1
        print("Progress: "+str(count)+"/"+str(len(new_posts)))