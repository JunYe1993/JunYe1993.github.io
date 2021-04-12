!['ProgrammerLife.jpg'](https://junye1993.github.io/image/ProgrammerLife.jpg)

## Navigating the tree - Going down

- **child Tag**

    前一篇呼叫 Tag 底下的 subTag 是用像 class 的方式 (Tag.subTag)，沒完整說明的是這個 subTag 可呼叫到的範圍並不只侷限 children Tag，而是整個 Tag 底下第一個遇到的 Tag.name == subTag。

``` python
    """ html
    <b class="boldest" id="bold man">
        <u>Extremely bold</u>
    </b>
    <p>Just a paragraph</p>
    """
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.u)  # <u>Extremely bold</u>
```

- **find_all()**

    依循前面的 subTag 找法，find_all 則會找出所有的 Tag (Tag.name == subTag)。

``` python
    soup.find_all('a')
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

- **.contents**

    Tag.contents 回傳包含所有 child string 的 list。

``` python
    print(soup.contents)  # [<d class="car"><u>Extremely bold.</u></d>, <p>123</p>]
```

- **.children**

    Tag.children 回傳包含所有 child Tag object 的 list。

``` python
    for child in soup.children:
        print(child.name)
    # b
    # p
```

- **.descendants**

    回傳一個不只包含 Tag 底下一層的 subTag，而是整個 tree 上所有 object。底下的結果之所以會有 None，是因為 NavigableString 也是 child 的包含範圍 ( .contents 跟 .children 也一樣 )，而 NavigableString object 沒有 .name。

``` python
    for child in soup.descendants:
        print(child.name)
    # b
    # u
    # None
    # p
    # None
```

- **.string**

    回傳底下唯一一個的 NavigableString 。如果 Tag 只有一個 child 而且還是 NavigableString 則回傳。如果 Tag 只有一個 child 且 child 也只有一個 NavigableString child 也是回傳。如果有兩個以上的 NavigableString 則要呼叫 .strings，.string 會回傳 None。

``` python
    print(soup.u.string) # Extremely bold
    print(soup.b.string) # Extremely bold
    print(soup.string)   # None
```

- **.strings & .stripped_strings**

    strings 會回傳所有 NavigableString。但這種情況下仍會紀錄到一些換行或字串前後的空格，所以可以用 stripped_strings 回傳乾淨的 NavigableString list。(如果整個字串都是空格或換行，則這個 NavigableString 會被無視)

``` python
    for sstr in soup.strings:
        print(repr(sstr))
    # 'Extremely bold'
    # 'Just a paragraph' 
```

## Navigating the tree - Going Up

- **.parent & .parents**

    基本上就是往上一層的 Tag (Soup 的 parent 為 None)。

``` python
    link = soup.a
    link
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    for parent in link.parents:
        print(parent.name)
    # p
    # body
    # html
    # [document]
```

## Navigating the tree - Going sideways

- **.next_sibling &.previous_sibling**

    往前找跟往後找，但是要注意的是他沒那方便幫你找到下一個或上一個的 Tag object，絕大部分都是 NavigableString，例如換行 (\n) 之類的。

``` python
    tag1 = soup.b
    tag2 = soup.p
    print(tag1.next_sibling)     # <p>123</p>
    print(tag2.previous_sibling) # <b class="boldest" id="bold man"><u>Extremely bold</u></b>
```

參考資料 :

1.[Beautiful Soup 4.9.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)