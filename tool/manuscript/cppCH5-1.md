!['Note.jpg'](https://junye1993.github.io/image/Note.jpg)

## Statement

- **Simple Statements**

    expression 加上 ; 作為結尾視為 statement。

``` c++
    a + 5  // expression
    a + 5; // statement
    ;      // null statement
```

- **Compound Statements (Blocks)**

    在 { } 中間一連串的 statements 或 declarations (也允許是空的)，且不用 ; 作為中止符。

``` c++
    while (val <= 10) {
        sum += val;  // assigns sum + val to sum
        ++val;       // add 1 to val
    }
```

- **Statement Scope**

    我們可以在 if else for 等等的 statements 裡宣告參數，但該參數也只有在 statements 裡能存取。

``` c++
    while (int i = get_num()) // i is created and initialized on each iteration
        cout << i << endl;
    i = 0;  // error: i is not accessible outside the loop
```

- **Conditional Statements**

    有 if statement, if else statement 和 switch statement。以下面的 switch code 為示範，"switch (ch)" 的 ch 為 expression，"case 'a':", "case 'e':" ... 為 case label，*當 expression match case label，execution 就會從此開始直到 switch 的中止符或 break*，所以是有可能橫跨 case labels。合法 case label 為 integral constant expressions，也就是 integral type 的 [constant expression](https://junye1993.blogspot.com/2020/07/c-primer-5th-edition-chapter-2-2.html)。

``` c++
    int vowelCnt = 0
    // any occurrence of a, e, i, o, or u increments vowelCnt
    while (cin >> ch) {
        switch (ch) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
                ++vowelCnt;
                break;
        }
    }
```

- **Why can't variables be declared in a switch statement?**

    首先這是 [stackoverflow][1] 裡的一個問題，問題題目應該改成 Why can't variables be *initialized* in a switch statement?，因為如果只有 declared 是合法的，頂多有 warning。*基本上 case 就是 label 的一種，一種常見於有 goto 的程式碼。若你做 variable definition 在 switch statement，等於在這 switch statement scope 裡會有機會因為做了 goto label 的關係而忽略掉該 definition，進而導致程式碼出錯。*若要在 switch statement 做 variable definition，你就必須很明確地告訴 compiler 即使有 goto label 忽略該 variable definition 也沒差，因為我只會在那 case 裡使用，也就是*加 {} 更近一步明確地縮小 variable definition 的 scope* 而非整個 switch statement scope。([Declaration跟Definition間的差異](https://junye1993.blogspot.com/2020/07/c-primer-5th-edition-chapter-2-1.html))

``` c++
    // Ok, 程式碼寫得漂亮，compiler 發現沒有任何 label 會忽略掉 init 的 definition
    switch (num) {
        case 1:
            int init = 0;
            cout << declare << endl;
    }
```

``` c++
    // Error, case 2 這個 label 會忽略 init 的 definition
    // main.cpp:17:10: error: jump to case label
    // 17 |     case 2:
    //    |          ^
    switch (num) {
        case 1:
            int init = 0;
            cout << init << endl;
        case 2:
            cout << 9999 << endl;
    }
```

``` c++
    // 加 {}，縮小該 variable definition 的 scope
    switch (num) {
        case 1:
            {
                int init = 0;
                cout << init << endl;
            }
        case 2:
            cout << 9999 << endl;
    }
```

``` c++
    // 只是 declaration 不會有事
    // 甚至因為是同 scope 所以 case 2 可以呼叫到
    // declare = 5; 若拿掉會出錯
    // 因為 compiler 發現 declare 從沒被賦予值過
    int num = 2;
    switch (num) {
        case 1:
            int declare;
            declare = 5;
        case 2:
            cout << declare << endl;
    }
    // Output: 21911
```

- **Iterative Statements**

    有 while statement, for statement 跟 do while Statement。C++ 的 for statement 除了傳統的還有 range for statement。其中 expression 必須要是 braced initializer list, array, vector 或 string 其中一種。

``` c++
    for (declaration : expression)
        statement
```

- **Jump Statements**

    有 break statement, continue statement 和 goto Statement。

參考資料 :
1.[why-cant-variables-be-declared-in-a-switch-statement][1]

[1]: https://stackoverflow.com/questions/92396/why-cant-variables-be-declared-in-a-switch-statement