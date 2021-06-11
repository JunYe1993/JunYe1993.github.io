!['Note.jpg'](https://junye1993.github.io/image/Note.jpg)

## Array

Array 為資料結構且跟 Vector 很像，都是裝同一 Type object 的 container。但 Array 為固定大小，所以不能增加 element，但也因為如此有時能提供較好的 run-time performance。

- **Initialize**

    在 C++ 裡 Array 的 Size 要為 constant expression，也就是 expression 能在 compile time 就算出來。*但因為 C 支援在 Array Size 塞變數，所以 G++ 將此寫法視為一個 extension，只要你不在 compile 時強調要遵循 C++ 的 Rule (-pedantic)。*

``` c++
    unsigned cnt = 42;            // not a constant expression
    constexpr unsigned sz = 42;   // constant expression
                                
    int arr[10];                  // array of ten ints
    int *parr[sz];                // array of 42 pointers to int
    string bad[cnt];              // error: cnt is not a constant expression
    string strs[get_size()];      // ok if get_size is constexpr, error otherwise
    int a1[3] = {0, 1, 2};        // [0, 1, 2]
    int a2[]  = {0, 1, 2};        // [0, 1, 2]
    int a3[5] = {0, 1, 2};        // [0, 1, 2, 0, 0]
    string a4[3] = {"hi", "bye"}; // ["hi", "bye", ""]
```

    賦予初始值可用 string 來直接 Initialize。

``` c++
    char a1[] = {'C', '+', '+'};       // list initialization, no null
    char a2[] = {'C', '+', '+', '\0'}; // list initialization, explicit null
    char a3[] = "C++";                 // null terminator added automatically
    const char a4[6] = "Daniel";       // error: no space for the null!
```

    加入 pointer 和 reference 的宣告

``` c++
    int *ptrs[10];            // ptrs is an array of ten pointers to int
    int &refs[10] = /* ? */;  // error: no arrays of references
    int (*Parray)[10] = &arr; // Parray points to an array of ten ints
    int (&arrRef)[10] = arr;  // arrRef refers to an array of ten ints
    int *(&arry)[10] = ptrs;  // arry is a reference to an array of ten pointers
```

- **Iterate**

    這裡紀錄像 Iterator 的方法。*arr\[10\] 是一個不存在的 index 所以只能取 address，所以當 pointer 指到它時就代表此 Array 已結束，類似 begin 跟 end 的方法。但這是較危險的寫法*

``` c++
    int arr[] = {0,1,2,3,4,5,6,7,8,9};
    int *e = &arr[10];
    for (int *b = arr; b != e; ++b)
        cout << *b << endl; // print the elements in arr
```     

    有 function 可以直接用。

``` c++
    int arr[] = {0,1,2,3,4,5,6,7,8,9}; 
    int *pbeg = begin(arr); // pbeg points to the first
    int *pend = end(arr);   // pend points just past the last element in arr
    for (int* p = pbeg; p != pend; ++p)
        cout << (*p) << endl;
```

- **Using an Array to Initialize a vector**

``` c++
    int int_arr[] = {0, 1, 2, 3, 4, 5};
    // ivec has six elements; each is a copy of the corresponding element in int_arr
    vector<int> ivec(begin(int_arr), end(int_arr));
    // copies three elements: int_arr[1], int_arr[2], int_arr[3]
    vector<int> subVec(int_arr + 1, int_arr + 4);
```

- **Initializing the Elements of a Multidimensional Array**

``` c++
    int ia[3][4] = {    // three elements; each element is an array of size 4
        {0, 1, 2, 3},   // initializers for the row indexed by 0
        {4, 5, 6, 7},   // initializers for the row indexed by 1
        {8, 9, 10, 11}  // initializers for the row indexed by 2
    };
    // equivalent initialization without the optional nested braces for each row
    int ia[3][4] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    // explicitly initialize row 0; the remaining elements are value initialized
    int ix[3][4] = {0, 3, 6, 9};
```

參考資料 :

1.[Initializing array with variable vs real number](https://stackoverflow.com/questions/15013077/arrayn-vs-array10-initializing-array-with-variable-vs-real-number)