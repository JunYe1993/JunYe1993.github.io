!['ProgrammerLife.jpg'](https://junye1993.github.io/image/ProgrammerLife.jpg)

## 讀檔時 UnicodeDecodeError: 'cp950' codec can't decode

老實說這非常常見，即使你的檔案是用 UTF-8 編寫，而且用 Python3 ( 絕大部分 default 是 utf-8 )，仍會報這個錯。所以要避免程式能在不同平台都能正常使用，讀檔時最好都加上 encoding="utf-8"

``` python
    with open("somefile.py", encoding="utf-8") as f:
        f.read()
```

參考資料 :

1.[stackoverflow](https://stackoverflow.com/questions/49021589/how-do-i-fix-this-cp950-illegal-multibyte-sequence-unicodedecodeerror-when-rea)