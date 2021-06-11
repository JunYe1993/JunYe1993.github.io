!['Note.jpg'](https://junye1993.github.io/image/Note.jpg)

## Exceptions

Exceptions 是程式在 run-time 遇到的異常，比如與資料庫的連結斷開或遇到其他程式異想不到的 input。Exception handling 基本上就是當程式無法解決問題或者無法繼續執行時發出警告，或者更進一步根據情況處理 exception。

Exception handling 由 detecting, handling parts of a program 所組成

- throw expressions

    當 detecting part 表示遭遇無法處理的情況

- try blocks

    handling part 用來處理 exception。程式碼一開始會有一個 try block 隨後跟著一個或以上的 catch clauses。

- exception classes

    用來傳遞 information about what happened between a throw and an associated catch.

## A throw Expression

通常會在 detecting part 發生 exception 時 throw Expression，這麼做原因是有時你不能保證你的程式一定是跟 User 互動的那一個，throw Expression 效果就比你回傳一個錯誤值好用得多。

``` c++
    // Normal version
    int throwTest(int num1, int num2) {
        if (num1 == num2) {
            cout << "Same." << endl;
            return 0;
        } else {
            cerr << "Not the same." << endl;
            return -1;
        }
    }

    // throw Expression
    void throwTest(int num1, int num2) {
        if (num1 != num2)
            throw runtime_error("Not the same.");
        cout << "Same." << endl;
    }
```

## The try Block

基於 C 風格的錯誤處理，在回傳值代表發生錯誤時予以處理。相比之下 throw 就相對靈活，但也會有終止程式的代價。try catch 的 block 就適合在此情況使用。讓程式有 exception handler。

``` c++
    try {
        program-statements
    } catch (exception-declaration) {
        handler-statements
    } catch (exception-declaration) {
        handler-statements
    } // . . .
```

## Standard Exceptions

正如上面的 try block 示億程式碼所示，程式必須先宣告 exception 的種類才能近一步去做 handle，這裡紀錄 C++ standard library \<stdexcept> 裡的 exception table。 

``` c++
    exception         // The most general kind of problem.

    // Runtime errors
    runtime_error     // Problem that can be detected at the run-time.
    range_error       // Result generated outside the range of value that are meaningful.
    overflow_error    // Computation that overflow.
    underflow_error   // Computation that underflow.
    
    // Logic errors
    logic_error       // Error in the logic of the program.
    domain_error      // Argument for which no result exists.
    invalid_argument  // Inappropriate argument.
    length_error      // Attempt to create an object larger than the maximum size for that type.
    out_of_range      // Use a value outside the valid range.
```
