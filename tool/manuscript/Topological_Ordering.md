!['Tree.jpg'](https://junye1993.github.io/image/Tree.jpg)

## Directed Acyclic Graph (DAG) 介紹

不同於 Tree 的無方向、無環，DAG 則是*有方向*、*無環*。DAG 特性是不斷地前進，有時分流、有時合流，日常常見的 DAG 為族譜、水流以及[課程擋修規則][1]。

## 實作

- **Topological Ordering**

    拿課程擋修規則為例，有必須先修的課程及後修的課程，將其完整排列出來視為 Topological Ordering。

``` c++
    // 課程 1 須先修 : None
    // 課程 2 須先修 : 課程 1
    // 課程 3 須先修 : 課程 1, 課程 2
    // 課程 4 須先修 : None
    // 
    // Gragh:
    // 課程 1 -> 課程 2
    //        ↘   ↓
    // 課程 4    課程 3
    //
    // Topological Ordering:
    //  1) 1 2 3 4
    //  2) 4 1 2 3
    //  3) 1 4 2 3
    //  4) 1 2 4 3
    // 兩個都行，只要順序符合規則就好 (按這個例子，課程 4 的排序位置無關緊要)
```

- **Topological Sort ( Kahn's Algorithm  )**

    排序時，首先要找到第一個點 (課程 1 或課程 4)。第一個點有一個特別之處，就是*沒有人指向他*。找出來該第一點後，把其指向的連接也跟著去掉。使下一次課程 2 變為第一個點。以此排序。

```c++
    // Gragh:
    //         課程 2
    //           ↓
    // 課程 4   課程 3
```

- **Code**

    [題目][1]之範例解答

``` c++
    bool canFinish (int numCourses, vector<vector<int>>& prerequisites) {
        
        // Kahn's Algorithm
        // http://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html

        // adj 紀錄 node 連出去的所有 nodes
        // ref 紀錄 node 被連的次數
        vector<vector<int>> adj(numCourses, vector<int>());
        vector<int> ref(numCourses, 0);
        
        // init
        for (auto&v : prerequisites) {
            ++ref[v[0]];
            adj[v[1]].push_back(v[0]);
        }

        // Every loop 都可以找到一個 first node, 需要找出 numCourses 個
        for (int i = 0; i < numCourses; ++i) {
            
            // 一定有 node 的被連的次數為 0, 是為 first node
            // 若所有 node 被連次數都 > 0, 代表有 cycle
            int head = 0;
            while (head < numCourses && ref[head] != 0) ++head;
            if (head == numCourses) return false;

            // 找過的 first node 要刪除, 設為 -1
            // 把這次的 first node 所連出去 nodes 的 被連次數(ref) 減一
            ref[head] = -1;
            for (auto & n : adj[head]) --ref[n];
        }

        return true;
    }
```

參考資料 :

1.[leetcode-problem-course-schedule][1]

2.[http://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html][2]

[1]: https://leetcode.com/problems/course-schedule/
[2]: http://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html