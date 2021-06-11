!['Note.jpg'](https://junye1993.github.io/image/Note.jpg)

## Expression

運算式 (expression) 由運算元 (operand) 與運算子 (operator) 所組成，最終計算產生一個結果 (result)。

- **Order of Evaluation**

    想要計算 expression 的話，就必須知道運算子運作及其先後順序。這裡的 * 號就不是 pointer 而是相乘，然後再來是基本的先乘除後加減。

``` c++
    cout << 5 + 10 * 20 / 2 << endl;        // 105
    cout << 6 + 3 * 4 / 2 + 2 << endl;      // 14
    cout << (6 + 3) *  (4 / 2 + 2) << endl; // 36
    cout << ((6 + 3) *  4) / 2 + 2 << endl; // 20
    cout << 6 + 3 * 4  / (2 + 2) << endl;   // 9
```

- **Lvalues and Rvalues**

    有寫過一篇 [Lvalues and Rvalues](https://junye1993.blogspot.com/2020/05/cc-lvaluervalue.html) 也可以參考。這裡紀錄此書寫大概的定義，*當我們將一個 object 視為 rvalue 使用，使用的是此 object 的值 (contents)。當我們將一個 object 視為 lvalue 使用，使用的是此 object 的「存在」(記憶體位置)。*還有一點也很重要，*lvalue 可以代替 rvalue，但反之 rvalue 卻不能代替 lvalue。*

``` c++
    int a = 1;     // a = lvalue, 1 = rvalue
    int b = a + 1; // a = lvalue, a = rvalue (lvalue 代替 rvalue)
    int 1 = a;     // Error, 1 != lvalue (rvalue 不能代替 lvalue)
```

## Operators

- **Logical and Relational Operators**

    Logical Operators 和 Relational Operators 回傳 bool。Logical Operators AND 跟 OR 永遠都會先計算左側再來計算右側。*這裡想特別紀錄的是 && 跟 ||，&& 代表只有左側計算出來是 True 才會計算右側，|| 則是只有左側計算出來是 False 才會計算右側*。這可以寫出一些流程控制而不是使用典型的 if else。Relational Operators 則是 >, <, >=, <=, ! 這些。

``` c++
    // 以下這兩個 val 都會被轉換成 bool
    if (val)  { /*  ...  */ } // true if val is any nonzero value
    if (!val) { /*  ...  */ } // true if val is zero
    
    // 有了上面兩個例子，我們看似可以將其改寫成以下寫法
    if (val == true) { /*  ...  */ }
    
    // 這個會產生問題，只要 val 的型別不是 bool
    // 假設 val 是 int，true 會被轉換成 int 也就是 1 跟原先的任何 nonzero value 相去甚遠
    if (val == 1) { /*  ...  */ } // true if val is 1
```

- **Assignment Operators**

    最常見就是等號 (=)。Assignment 是 Right Associative，以下有程式碼示範。另外 Assignment Operators 執行順序較低通常會用括弧輔助。

``` c++
    int ival, jval;
    ival = jval = 0; // ok: each assigned 0
    // 對於右邊的 assignment，jval = 0
    // 對於左邊的 assignment，ival = (jval = 0)
    // jval assigned 0 後，回傳 jval (ival = jval)，ival = 0
```

``` c++
    // 原先邏輯
    int i = get_value();
    while (i != 42) {
        // do something ...
        i = get_value();
    }
    // 改寫，用括弧輔助
    int i;
    while ((i = get_value()) != 42) {
        // do something ...
    }
```

- **Increment and Decrement Operators**

    ++ -- 用來做 Increment 和 Decrement，兩個都有 prefix 跟 postfix 的寫法，效果如下程式碼示範。*要注意的是要盡量用 prefix 來做運算，因為你通常不會需要做增減前的 value，而 postfix 會 copy 一份增減前的 value 來做回傳。* 

``` c++
    int i = 0, j;
    j = ++i; // j = 1, i = 1: prefix yields the incremented value
    j = i++; // j = 1, i = 2: postfix yields the unincremented value

    // 需要 postfix 的場合
    auto pbeg = v.begin();
    // print elements up to the first negative value
    while (pbeg != v.end() && *beg >= 0)
        cout << *pbeg++ << endl; // print the current value and advance pbeg
```

    Operand 運算順序不是固定的，通常不會造成問題，但如果兩邊有用到同一 variable 且用了 Increment 或 Decrement Operators 問題就會浮現。

``` c++
    // 原先邏輯是把 s 裡的 char 都改成大寫
    // the behavior of the following loop is undefined!
    auto it = s.begin()
    while (it != s.end() && !isspace(*it))
        *it = toupper(*it++);   // error: this assignment is undefined

    // 會有兩種結果
    // 第一種輸出 ABCDEFG
    *beg = toupper(*beg);        // 先執行左邊的 Operand，Output: ABCDEFG
    *(beg + 1) = toupper(*beg);  // 先執行左邊的 Operand，Output: aAAAAAA
```

- **Shift Operators (aka IO Operators) Are Left Associative**

``` c++
    cout << "hi" << " there" << endl;
    ( (cout << "hi") << " there" ) << endl;

    cout << 42 + 10;   // ok: + has higher precedence, so the sum is printed
    cout << (10 < 42); // ok: parentheses force intended grouping; prints 1
    cout << 10 < 42;   // error: attempt to compare cout to 42!
```