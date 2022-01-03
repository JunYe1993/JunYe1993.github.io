!['ProgrammerLife.jpg'](https://junye1993.github.io/image/ProgrammerLife.jpg)

## map vs unordered_map

在 C++ 裡有標題的兩種 Hash table 可以使用，兩種在不同的領域上效率上有很大的差異。不信可以去看用到 map 的 leetcode problem 裡其他使用者的答案，多半是 unordered_map。

## 效率比較

擷取自[GeeksforGeeks][1]

```
                    | map                 | unordered_map
    ---------------------------------------------------------
    Ordering        | increasing  order   | no ordering
                    | (by default)        |

    Implementation  | Self balancing BST  | Hash Table
                    | like Red-Black Tree |  

    search time     | log(n)              | O(1) -> Average 
                    |                     | O(n) -> Worst Case

    Insertion time  | log(n) + Rebalance  | Same as search
                        
    Deletion time   | log(n) + Rebalance  | Same as search
```

## 我的結論

map 是穩定的平衡樹，可以因應許多要求。例如 key 的排序或增減，其穩定度都很好。但是 leetcode 裡大部分都是扮演輔助的角色，其最常出現的就是樣子就是 map\<char, int>，單純去算 char 出現的次數。而非像字典一樣紀錄無數的 key。

- **unordered_map** 
    
    單純算出現次數

- **map** 

    建立複雜的資料庫

參考資料 :

1.[geeksforgeeks][1]

[1]: https://www.geeksforgeeks.org/map-vs-unordered_map-c/