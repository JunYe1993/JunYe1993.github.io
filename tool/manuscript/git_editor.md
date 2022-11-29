!['Git.jpg'](https://junye1993.github.io/image/Git.jpg)

## Git editor

大部分遇到 Git editor 都是在 commit 的時候。這邊紀錄一下設定。

## Git setting

    核心概念是去修改 git config > global > core > editor。

``` bash
    # vscode 在 ubuntu 底下就是 code
    git config --global core.editor 'code'
```

    但這會遇到以下問題。

``` bash
    # 更改 editor 成 vscode
    JunYe1993:~/project/JunYeGit$ git config --global core.editor 'code'
    # 作一次簡單的 commit, 發現沒有用
    JunYe1993:~/project/JunYeGit$ git add .
    JunYe1993:~/project/JunYeGit$ git commit
    Aborting commit due to empty commit message.
```

    主要原因是你的 Terminal 在執行 git commit 彈出視窗後就 return 了，所以 COMMIT_EDITMSG 會是空的，commit failed。解決的方法是使用 code 的 option "-w --wait" (Wait for the files to be closed before returning)。所以等你編輯完關閉 COMMIT_EDITMSG 就 OK 了。

``` bash
    JunYe1993:~/project/JunYeGit$ git config --global core.editor 'code --wait'
    JunYe1993:~/project/JunYeGit$ git commit
    hint: Waiting for your editor to close the file...
```

參考資料 :
1.[vscode-git][1]

[1]: https://www.roboleary.net/vscode/2020/09/15/vscode-git.html