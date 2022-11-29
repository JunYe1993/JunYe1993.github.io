!['Note.jpg'](https://junye1993.github.io/image/Note.jpg)

## Library - vector

- **Intro**

    vector 是物件的集合，集合裡的物件都是同一 type，且每個物件都有 index 可以用找到該物件。vector 也是 container 和 class template 的一種。

``` c++
    vector<int> ivec;             // ivec holds objects of type int
    vector<Sales_item> Sales_vec; // holds Sales_items
    vector<vector<string>> file;  // vector whose elements are vectors
```

- **Initialize**

``` c++
    vector<int> ivec;               // initially empty
    // give ivec some values
    vector<int> ivec2(ivec);        // copy elements of ivec into ivec2   
    vector<int> ivec3 = ivec;       // copy elements of ivec into ivec3   
    vector<string> svec(ivec2);     // error: svec holds strings, not ints
    vector<int> ivec(10, -1);       // ten int elements, each initialized to -1
    vector<string> svec(10, "hi!"); // ten strings; each element is "hi!"
```

- **Add**

    push_back 會在 run time 的時候執行，會加 object 到 container 的最後端

``` c++
    vector<int> v2;        // empty vector
    for (int i = 0; i != 100; ++i)
        v2.push_back(i);    // append sequential integers to v2
    // at end of loop v2 has 100 elements, values 0 . . . 99
```

- **Operations**

``` c++
    v.empty()       // Return true if v is empty; otherwise return false.
    v.size()        // Return the number of elements in v.
    v.push_back(t)  // And an element with value t to end of v.
    v[n]            // Return a reference to the element at position n in v
    v1 = v2         // Replaces the elements in v1 with a copy of the elements in v2
    v1 = {a,b,c...} // Replaces the elements in v1 with a copy of the elements in the comma-separated list
    v1 == v2        // v1 and v2 are equal if they have same number of elements and each
    v1 != v2        // element in v1 is equal to the corresponding element in v2
```

## Library - iterators

- **Intro**

    雖然使用者可以用 \[n\] (subscripts) 來取得 string 或 vector 的 element。但有一個更通用的用法也就是 iterator。

- **Using**

    不像 pointer 不是用 address-of operator 來獲取 iterator，有些型別本身就有成員回傳 iterator。典型就是行別有成員 begin 和 end。*begin 指向第一個 element，而 end 指向的是 container 的"結束"，也就是說當 container 的 element 數量為 0 時，begin == end。*

``` c++
    // the compiler determines the type of b and e;
    // b denotes the first element and e denotes one past the last element in v
    auto b = v.begin(), e = v.end(); // b and e have the same type
```

- **Operation**

``` c++
    *iter       // Return a reference to the element denoted by the iterator iter
    iter->mem   // Dereferences iter and fetches the member named mem from the
                // underlying element. Equivalent to the (*iter).mem
    ++iter      // Refers to the next element in the container
    --iter      // Refers to the previous element in the container
```

    利用 begin() != end() 來確認不是空字串

``` c++
    string s("some string");
    if (s.begin() != s.end()) { // make sure s is not empty
        auto it = s.begin();    // it denotes the first character in s
        *it = toupper(*it);     // make that character uppercase
    }
```

- **Iterates through the elements in container**

    這裡用 string 示範，比較要注意的是*常用的迴圈終止條件用的是 != end()，而非用往常的 < 。並不是所有 Iterator 都可以支援 < operator*，剛好 vector 還有 string 支援而已。

``` c++
    // process characters in s until we run out of characters or we hit a whitespace
    for (auto it = s.begin(); it != s.end() && !isspace(*it); ++it)
        *it = toupper(*it); // capitalize the current character
```

- **Type**

    如果想要精準宣告 Iterator 的 Type 的話。

``` c++
    vector<int>::iterator it;        // it can read and write vector<int> elements
    string::iterator it2;            // it2 can read and write characters in a string
    vector<int>::const_iterator it3; // it3 can read but not write elements
    string::const_iterator it4;      // it4 can read but not write characters
```

- **Operations Supported by vector and string Iterators**

    上面有提到 vector 跟 string 的 iterator 有支援較多的 operator。

``` c++
    // The iterators must denote element in, or one past the end of, the same container

    iter + n      // Adding (subtracting) an integral value n to (from) an iterator yields an
    iter - n      // iterator that many elements forward (backward) within the container.

    iter1 += n    // Compound-assignment for iterator addition. 
    iter1 -= n    // Compound-assignment for iterator subtraction.

    iter1 - iter2 // Subtracting two iterators yields the number that when added to the
                  // right-hand iterator yields the left-hand iterator.

    >, <=, <, <=  // Relational operators on iterators. One iterator is less than another if it
                  // refers to an element that appears in the container before the referred to 
                  // by the other iterator.
```

    取中間的 iterator

``` c++
    // compute an iterator to the element closest to the midpoint of vi
    auto mid = vi.begin() + vi.size() / 2;
```

    binary search

``` c++
    // text must be sorted
    // beg and end will denote the range we're searching
    auto beg = text.begin(), end = text.end();
    auto mid = text.begin() + (end - beg)/2; // original midpoint
    // while there are still elements to look at and we haven't yet found sought
    while (mid != end && *mid != sought) {
        if (sought < *mid)     // is the element we want in the first half?
            end = mid;         // if so, adjust the range to ignore the second half
        else                   // the element we want is in the second half
            beg = mid + 1;     // start looking with the element just after mid
        mid = beg + (end - beg)/2;  // new midpoint
    }
```