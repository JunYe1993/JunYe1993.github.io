from bs4 import BeautifulSoup

def picPrettify (soup):
    for img in soup.find_all("img"):

        img['border'] = 0
        img['data-original-height'] = 1365
        img['data-original-width'] = 2048
        img['height'] = 426

        div = img.parent
        div.name = "div"
        div['class'] = "separator"
        div['style'] = (
            "clear: both;",
            "text-align: center;"
        )

        a = soup.new_tag("a")
        content = img.replace_with(a)
        a.append(content)
        a['style'] = (
            "margin-left: 1em;",
            "margin-right: 1em;"
        )

def h2Prettify (soup):
    for h2 in soup.find_all("h2"):
        h2['style'] = (
            "background-color: #e6edeb;",
            "border-left: 5px solid rgb(2, 180, 206);",
            "box-sizing: border-box;",
            "font-size: large;",
            "letter-spacing: 1.44px;",
            "line-height: 1.6em;",
            "margin: 16px 0px 12px;",
            "padding: 10px 10px 10px 18px;",
            "text-align: justify;"
        )

def refBlockPrettify (soup):
    for referenceTitle in soup.find_all("p"):
        if referenceTitle.string == "參考資料 :":
            referenceTitle['style'] = "margin-top: 36px;"                  

def myBloggerPrettify (html) -> str:
    soup = BeautifulSoup(html, features="html.parser")
    
    # implement my blog style
    picPrettify(soup)
    h2Prettify(soup)
    refBlockPrettify(soup)

    return soup.prettify()