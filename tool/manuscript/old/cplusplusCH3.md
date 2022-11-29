!['Note.jpg'](https://junye1993.github.io/image/Note.jpg)

## Namespace - using declaration

為了讀取 stdin，程式碼會是 std::cin。 :: 的左邊是告訴 compiler 去哪個 scope 找右邊的 operand。這有時會造成程式碼過於冗長，所以有了 using declaration 讓你更簡單的呼叫 namespace 底下的成員。

``` c++
    #include <iostream>
    using std::cin;
    int main()
    {
        int i;
        cin >> i;       // ok: cin is a synonym for std::cin
        cout << i;      // error: no using declaration; we must use the full name
        std::cout << i; // ok: explicitly use cout from namepsace std
        return 0;
    }
```

using declaration 通常不會出現在 header 裡，因為 header 會被複製到各個程式中，會導致所有 include 該 header 的程式用相同的 using declaration 容易造成命名衝突。

## Library - string

- **Initialize**

``` c++
    #include <string>
    using std::string;
    string s1;            // default initialization; s1 is the empty string
    string s2 = s1;       // s2 is a copy of  s1
    string s3 = "hiya";   // s3 is a copy of the string literal
    string s4(10, 'c');   // s4 is cccccccccc
```

- **std::cin interaction**

    cin 會因為 space 而被分開，以下程式碼若輸入 "Hello World!"，則 s1 = "Hello", s2 = "World!"

``` c++
    string s1, s2;
    cin >> s1 >> s2; // read first input into s1, second into s2
    cout << s1 << s2 << endl; // write both strings
```

    可以用 getline 來讀完整的 "Hello World!"

``` c++
    string line;
    // read input a line at a time until end-of-file
    while (getline(cin, line))
        cout << line << endl;
    return 0;
```

- **Comparing & Adding Two string**

    string 可以使用 ==, != 做比較，也可以用 + 來做字串串接

``` c++
    string s1 = "hello, ", s2 = "world\n";
    string s3 = s1 + s2;   // s3 is hello, world\n
    s1 += s2;   // equivalent to s1 = s1 + s2
```

- **Iterates through the chars in a string**

    可以用 for(auto c : str)，也可以用 for(auto &c : str)。&c 是 reference 所以可以改變 str 裡的 char。 

``` c++
    string str("some string");
    // print the characters in str one character to a line
    for (auto c : str)      // for every char in str
        cout << c << endl;  // print the current character followed by a newline
```