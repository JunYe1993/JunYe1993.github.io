!['Tree.jpg'](https://junye1993.github.io/image/Development.jpg)

## 使用 vscode 自動刪除空格的原因

當你上 code 時，有 reviewer 看你的程式碼時，通常會用 meld 等軟體 review。當你的程式碼加了多餘的空格時，都會被這些程式碼 highlight，使得 reviewer 在查看你的程式碼時有一定的不便。

## vscode 刪除空格

- **手動刪除空格 (Remove trailing spaces manually)**

    <kbd>ctrl + alt + p</kbd>，輸入 trail 你應該就可以看到相關快捷鍵。

- **自動刪除空格 (Remove trailing spaces automatically)**

    <kbd>setting</kbd> > <kbd>右上角的 open setting (JSON)</kbd> > 加入以下這行。

``` JSON
    "files.trimTrailingWhitespace": true
```

參考資料 :

1.[remove-trailing-spaces-automatically-or-with-a-shortcut][1]

[1]: https://stackoverflow.com/questions/30884131/remove-trailing-spaces-automatically-or-with-a-shortcut