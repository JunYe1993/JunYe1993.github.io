from bs4 import BeautifulSoup

html = (
    '<b class="boldest" id="bold man">'
        '<u>Extremely bold</u>'
    '</b>'
    '<p>123</p>'
)
"""
<b class="boldest" id="bold man">
    <u>Extremely bold</u>
</b>
<p>Just a paragraph</p>
"""
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))   # <class 'bs4.BeautifulSoup'>
print(soup.b)       # <b class="boldest" id="bold man"><u>Extremely bold</u></b>
print(soup.p)       # <p>Just a paragraph</p>

# Tag 有兩個基礎參數 name 跟 attrs
tag = soup.b
print(type(tag))    # <class 'bs4.element.Tag'>
print(tag.name)     # b
print(tag.attrs)    # {'class': ['boldest'], 'id': 'bold man'}

# name 跟 attrs 都可以直接修改
tag.name = "d"
tag.attrs = {'class': ['boldest', 'cutest'], 'id': 'pui pui'}
print(str(tag))     # <d class="boldest cutest" id="pui pui"><u>Extremely bold</u></d>

#
print(str(tag.u))   # <u>Extremely bold</u>
print(tag['class']) # ['boldest', 'cutest']
print(tag['id'])    # pui pui

tag['class'] = ['car']
del tag['id']
print(str(tag))     # <d class="car"><u>Extremely bold</u></d>

# 
tag.u.string.replace_with("No longer bold.")
print(type(tag.u.string)) # <class 'bs4.element.NavigableString'>
print(str(tag.u.string))  # No longer bold.

print(str(soup))
print(soup.prettify())