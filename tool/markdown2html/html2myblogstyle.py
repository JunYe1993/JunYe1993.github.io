from bs4 import BeautifulSoup, NavigableString

CPP_PRIMER_CHAPTER_END = "-cpce"

def auditCodeBlock (soup):
    for code in soup.find_all("code"):
        pre = code.parent
        # pre between code blocks may be mistaken for code block, by library markdown.
        if not code.has_attr("class"):
            code.replace_with(code.string.strip())
            pre.name = "p"
    
        previous = pre.previous_sibling
        while isinstance(previous, NavigableString):
            previous = previous.previous_sibling
        if previous.name == "ul":
            li = None
            for child in previous.children:
                if child.name == "li":
                    li = child
            code['style'] = "width: 95%;"
            li.append(pre)
            

def picPrettify (soup):
    for img in soup.find_all("img"):
        img['border'] = 0
        img['data-original-height'] = 1365
        img['data-original-width'] = 2048
        img['height'] = 424
        img['width'] = 640

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

def emPrettify (soup, option = None):
    for em in soup.find_all("em"):
        span = soup.new_tag("span")
        content = em.replace_with(span)
        b = soup.new_tag("b")
        span.append(b)
        b.append(content)
        span['style'] = "color: #e06666;"

def strongLiPrettify (soup, option = None):
    if option == CPP_PRIMER_CHAPTER_END:
        for strong in soup.find_all("strong"):
            # replace <strong></strong> to <b><u></u></b>
            b = soup.new_tag('b')
            content = strong.replace_with(b)
            b.append(content)
            b.strong.name = "u"
            
            parent = b.parent
            if parent.parent.name == "li":
                parent.name = "font"
                parent['face'] = "helvetica"
                parent['size'] = "5"
    else:
        for strong in soup.find_all("strong"):
            # replace <strong></strong> to <b><u></u></b>
            b = soup.new_tag('b')
            content = strong.replace_with(b)
            b.append(content)
            b.strong.name = "u"
            
            parent = b.parent
            if parent.name == "li":
                p = soup.new_tag('p')
                content = b.replace_with(p)
                p.append(content)
                p['style'] = "background-color: #fff7e9;"
            else:
                parent['style'] = "background-color: #fff7e9;"

def pPrettify (soup, option = None):
    if option == CPP_PRIMER_CHAPTER_END:
        for p in soup.find_all("p"):
            div = soup.new_tag('div')
            content = p.replace_with(div)
            div.append(content)
            div['style'] = "margin: 12px 0px 12px;"

            p.name = "span"
            p['style'] = (
                "background-color: #edf4e8;"
                "color: #111111;"
                "font-family: 'times new roman';"
                "font-size: 18px;"
                "font-style: italic;"
            )
    else:
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

# import re
# def codePrettify (soup):
#     data = soup.prettify()
#     normal_pattern = r'</li>\s*</ul>\s*(<pre><code[^<]*</code></pre>)'
#     middle_pattern = r'</li>\s*</ul>\s*(<pre><code[^<]*</code></pre>)\s*<ul>\s*<li>'
#     if re.search(normal_pattern, data):
#         if re.search(middle_pattern, data):
#             data = re.sub(middle_pattern, r'\1</li><li>', data)
#         if re.search(normal_pattern, data):
#             # print(re.findall(normal_pattern, ))
#             data = re.sub(normal_pattern, r'\1</li></ul>', data)
# 
#     soup = BeautifulSoup(data, features="html.parser")
#     for codeblock in soup.find_all("code"):
#         codeblock.string = codeblock.string[:-1]
#         if codeblock.parent.parent.name == "li":
#             codeblock['style'] = "width: 95%;"
#     
#     return soup

def myBloggerPrettify (html, option = None) -> str:
    soup = BeautifulSoup(html, features="html.parser")
    
    # implement my blog style
    if option == None: 
        auditCodeBlock(soup)
        picPrettify(soup)
        h2Prettify(soup)
        emPrettify(soup)
        strongLiPrettify(soup)
        pPrettify(soup)
        quotePrettify(soup)
        refBlockPrettify(soup)
    # for c++ chapter defined terms
    elif option == CPP_PRIMER_CHAPTER_END:
        picPrettify(soup)
        h2Prettify(soup)
        strongLiPrettify(soup, option)
        pPrettify(soup, option)

    return soup.prettify()