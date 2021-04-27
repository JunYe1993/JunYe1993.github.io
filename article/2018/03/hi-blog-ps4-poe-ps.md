!['Git.jpg'](https://junye1993.github.io/image/Git.jpg)

## Git - delete submodule

因為上網 Google 這問題你會發現[這個Stackoverflow][1]和[這個Github][2]的答案。很久以前查的時候 stackoverflow 置頂的答案是以前最多 upvote 的答案，也就是 [githb][2] 的答案。但 git 在版本更新後那個 7 步刪除 submodule 的已經過時了。雖然還是可以用但現在三步就可完成。

``` bash
    # 用 git submodule deinit 清除 git config 的紀錄
    git submodule deinit -f path/to/submodule

    # 手動刪除 git 不再 track 的 submodule file
    rm -rf .git/modules/path/to/submodule

    # 用 git 清除 .gitmodules 的紀錄
    git rm -f path/to/submodule
```

參考資料 :
1.[stackoverflow][1]

[1]: https://stackoverflow.com/questions/1260748/how-do-i-remove-a-submodule
[2]: https://gist.github.com/myusuf3/7f645819ded92bda6677