!['Tree.jpg'](https://junye1993.github.io/image/Tree.jpg)

## Segment-Tree 介紹

主要用來找*區間最大值*或*區間總和*。由於我是為了[這題][1]所以以區間總和做介紹。

``` c++
    // nums:[-1, 4, 2, 0, 5]
    //
    // Segment Tree for the Above Array:
    //
    //         10                     [0,4]
    //        /  \
    //      5      5           [0,2]          [3,4]
    //     / \    / \
    //    3   2  0   5      [0,1]  [2,2]   [3,3]  [4,4]
    //   / \   
    // -1  4            [0,0]  [1,1]
```

## Segment-Tree 實作

- **Build Tree**

    這邊我用 c++ 概略作介紹 ( a.k.a. compile 過不了 )。基本上是 top-down 的 build 法，時間複雜度為 O(n)。

``` c++
    // Node 資料結構
    struct segTreeNode {
        int begin;
        int end;
        int sum;
        segTreeNode* left;
        segTreeNode* right;
    }
```
``` c++
    // Build
    segTreeNode* buildSegTree(int begin, int end, vector<int>& nums) {
        // 若 begin = end，代表是 leaf。
        if (begin == end) return segTreeNode(begin,end,nums[begin],NULL,NULL);
        
        // 分割
        int mid = (begin + end) / 2;
        auto left = buildSegTree(begin, mid, nums);
        auto right = buildSegTree(mid+1, end, nums);
        return segTreeNode(begin, end, segTree, left.sum+right.sum, left, right);
        // 最後 return 的 node 為 root
    }
```

- **Update tree**

    時間複雜度為 O(log n)。

``` c++
    // Update
    segTreeNode updateSegTree(segTreeNode& node, int index, int val) {
        
        // 若是該 index 的 leaf。則更新其 sum
        if (node->begin == node->end && node->end == index) {
            node->sum = val;
            return;
        }

        // 若是中間 node 則分割往下繼續找
        int mid = (node->begin+node->end)/2;
        if (index > mid)
            updateSegTree(node->right, index, val);
        else
            updateSegTree(node->left, index, val);
        
        // 最後更新 node's sum
        node->sum = node->left->sum + node->right->sum;
    }
```

- **Update tree**

    時間複雜度為 O(log n)。

``` c++
    // Update
    segTreeNode updateSegTree(segTreeNode& node, int index, int val) {
        
        // 若是該 index 的 leaf。則更新其 sum
        if (node->begin == node->end && node->end == index) {
            node->sum = val;
            return;
        }

        // 若是中間 node 則分割往下繼續找
        int mid = (node->begin+node->end)/2;
        if (index > mid)
            updateSegTree(node->right, index, val);
        else
            updateSegTree(node->left, index, val);
        
        // 最後更新 node's sum
        node->sum = node->left->sum + node->right->sum;
    }
```

- **Sum**

    時間複雜度為 O(log n + k)。

``` c++
    // Sum
    int sum(segTreeNode& node, int left, int right) {
        
        // 若完美覆蓋區間，直接回傳。
        if (node->begin == left && node->end == right)
            return node->sum;

        int mid = (node->begin+node->end)/2;
        // 要求區間完全在左邊
        if (right <= mid)
            return sum(node->left, left, right);
        // 要求區間完全在右邊
        else if (left > mid)
            return sum(node->right, left, right);
        // 兩邊都有
        else
            return sum(node->left, left, mid) + 
                   sum(node->right, mid+1, right);
    }
``` 

參考資料 :

1.[leetcode/hg3994 answer][1]

2.[youtube 中文講解](https://www.youtube.com/watch?v=rYBtViWXYeI&ab_channel=HuaHua)

[1]: https://leetcode.com/problems/range-sum-query-mutable/
[2]: https://leetcode.com/problems/range-sum-query-mutable/discuss/1218358/C%2B%2B-or-Segment-Tree-or-Explained