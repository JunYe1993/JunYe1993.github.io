import re
from bs4 import BeautifulSoup, NavigableString

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
            "clear: both;"
            "text-align: center;"
        )

        a = soup.new_tag("a")
        content = img.replace_with(a)
        a.append(content)
        a['style'] = (
            "margin-left: 1em;"
            "margin-right: 1em;"
        )

def h2Prettify (soup):
    notFirst = False
    for h2 in soup.find_all("h2"):
        if notFirst:
            h2['style'] = (
                "background-color: #e6edeb;"
                "border-left: 5px solid rgb(2, 180, 206);"
                "box-sizing: border-box;"
                "font-size: large;"
                "letter-spacing: 1.44px;"
                "line-height: 1.6em;"
                "margin: 36px 0px 24px;"
                "padding: 10px 10px 10px 18px;"
                "text-align: justify;"
            )
        else:
            notFirst = True
            h2['style'] = (
                "background-color: #e6edeb;"
                "border-left: 5px solid rgb(2, 180, 206);"
                "box-sizing: border-box;"
                "font-size: large;"
                "letter-spacing: 1.44px;"
                "line-height: 1.6em;"
                "margin: 16px 0px 24px;"
                "padding: 10px 10px 10px 18px;"
                "text-align: justify;"
            )


def strongPrettify (soup):
    for strong in soup.find_all("strong"):
        # replace <strong></strong> to <b><u></u></b>
        b = soup.new_tag('b')
        content = strong.replace_with(b)
        b.append(content)
        b.strong.name = "u"
        
        p = b.parent
        p['style'] = "background-color: #fff7e9;"

def pPrettify (soup):
    for p in soup.find_all("p"):
        pre = soup.new_tag('pre')
        content = p.replace_with(pre)
        pre.append(content)

        pre['style'] = (
            "white-space: pre-wrap;"      # Since CSS 2.1
            "white-space: -moz-pre-wrap;" # Mozilla, since 1999
            "white-space: -pre-wrap;"     # Opera 4-6
            "white-space: -o-pre-wrap;"   # Opera 7
            "word-wrap: break-word;"      # Internet Explorer 5.5+
        )

        p.name = "font"
        p['face'] = "helvetica"
        p['size'] = 4

# Must call after pPrettify
def quotePrettify(soup):
    for quote in soup.find_all("blockquote"):
        font = quote.pre.font
        font['color'] = "#cc0000"

def refBlockPrettify (soup):
    refPart = False
    for font in soup.find_all("font"):
        if refPart or font.string == "參考資料 :": 
            font['size'] = 4.5
            if not refPart: 
                pre = font.parent
                pre['style'] += "margin-top: 36px;"
            refPart = True
    
def codePrettify (soup):
    data = soup.prettify()
    normal_pattern = r'</li>\s*</ul>\s*(<pre><code[^<]*</code></pre>)'
    middle_pattern = r'</li>\s*</ul>\s*(<pre><code[^<]*</code></pre>)\s*<ul>\s*<li>'
    if re.search(normal_pattern, data):
        if re.search(middle_pattern, data):
            data = re.sub(middle_pattern, r'\1</li><li>', data)
        if re.search(normal_pattern, data):
            # print(re.findall(normal_pattern, ))
            data = re.sub(normal_pattern, r'\1</li></ul>', data)

    soup = BeautifulSoup(data, features="html.parser")
    for codeblock in soup.find_all("code"):
        codeblock.string = codeblock.string[:-1]
        if codeblock.parent.parent.name == "li":
            codeblock['style'] = "width: 95%;"
    
    return soup

def myBloggerPrettify (html) -> str:
    soup = BeautifulSoup(html, features="html.parser")
    
    # implement my blog style
    picPrettify(soup)
    h2Prettify(soup)
    strongPrettify(soup)
    pPrettify(soup)
    quotePrettify(soup)
    refBlockPrettify(soup)
    soup = codePrettify(soup)
    
    return soup.prettify()