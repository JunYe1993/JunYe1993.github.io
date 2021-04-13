!['ProgrammerLife.jpg'](https://junye1993.github.io/image/ProgrammerLife.jpg)

## Common python module - sys

- **sys parameter**

    一些常見系統參數
```python
    import sys
    print(sys.platform) # linux
```
  
- **sys.argv**

    像 c/c++ 的 argv 一樣，可以吃從 command line 傳入的參數。
``` python
    # test.py 123 456 789
    print (argv)    # ['test.py', '123', '456', '789']
    print (argv[1]) # 123
```

- **sys.path**

    import 時的 search list，可以也透過改變(增加, 刪除, 更改順序) list 來在想要的位置 import。除了 built-in 的 lodule，其他額外安裝的 module 都可以用這個順序做調整。以下例子就等於會先去找 tool/ 底下的 module，找不到才會找 local/lib/python3.X/site-packages 或 local/lib/python3.X/dist-packages
``` python
    print (sys.path)            # [......]
    sys.path.insert(0, "tool/") # ['tool/',......] 
    import markdown             # 已安裝 markdown，但 import 的卻是 tool 底下的
    print(markdown.__file__)    # tool/markdown.py
```

## Common python module - os

- **os.function**

    一些常用的 os.function
``` python
    import os
    os.system(command)	# 執行 command ， command 為系統指令的字串。
    os.getcwd()	        # 取得目前所在路徑。
    os.rename(src, dst)	# 將 src 改名為 dst 。
    os.mkdir(path)	    # 建立 path 路徑，如果已存在就會發起例外。
    os.remove(path)	    # 移除 path ，如果 path 是目錄就會發起例外。
    os.rmdir(path)	    # 刪除 path 目錄。
```

- **os.path (1)**

    檢查檔案目錄。
``` python
    import os
    os.path.isfile(path)	        # 判斷 path 檔案是否存在。
    os.path.isdir(path)	            # 判斷 path 路徑是否存在。
```

- **os.path (2)**

    os.path 路徑處理。
``` python
    import os
    path = "/home/JunYe/123.txt"
    os.path.dirname(path)  # 回傳 path 的目錄路徑。
    os.path.basename(path) # 回傳 path 的檔案名稱。
    os.path.split(path)    # 分割路徑為 (head, tail) ，其中 head 為目錄， tail 為檔案名稱。
    os.path.splitext(path) # 分割路徑為 (root, ext) ，其中 root 為目錄包括檔名， ext 為副檔名。
    print(os.path.dirname(path))  # /home/JunYe
    print(os.path.basename(path)) # 123.txt
    print(os.path.split(path))    # ('/home/JunYe', '123.txt')
    print(os.path.splitext(path)) # ('/home/JunYe/123', '.txt')
```

參考資料 :

1.[sys — 你所不知道的 Python 標準函式庫用法 01](https://blog.louie.lu/2017/07/26/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-01-sys/)
2.[Python 速查手冊 - 12.5 基本檔案與目錄處理 os 與 os.path](http://kaiching.org/pydoing/py/python-library-ospath.html)