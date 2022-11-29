!['Note.jpg'](https://junye1993.github.io/image/Note.jpg)

## Type Conversions

- **Implicit Conversions**

    型別轉換，大部分轉換都是看是否能轉換成 int，例如 char, bool, 和 short。

``` c++
    bool      flag;   char           cval;
    short     sval;   unsigned short usval;
    int       ival;   unsigned int   uival;
    long      lval;   unsigned long  ulval;
    float     fval;   double         dval;
    3.14159L + 'a'; //  'a' promoted to int, then that int converted to long double
    dval + ival;    //  ival converted to double
    dval + fval;    //  fval converted to double
    ival = dval;    //  dval converted (by truncation) to int
    flag = dval;    //  if dval is 0, then flag is false, otherwise true
    cval + fval;    //  cval promoted to int, then that int converted to float
    sval + cval;    //  sval and cval promoted to int
    cval + lval;    //  cval converted to long
    ival + ulval;   //  ival converted to unsigned long
    usval + ival;   //  promotion depends on the size of unsigned short and int
    uival + lval;   //  conversion depends on the size of unsigned int and long
```

- **Explicit Conversions**

    用於我們想明確地強制將 object 轉換為其他類型。cast-name\<type>(expression)。([const相關文章1](https://junye1993.blogspot.com/2020/07/c-primer-5th-edition-chapter-2-2.html), [const相關文章2](https://junye1993.blogspot.com/2020/05/cc-const.html))

``` c++
    // static_cast 最常用的 cast-name
    // cast used to force floating-point division
    double slope = static_cast<double>(j) / i;

    // const_cast 用來改變 low-level const (point to const)
    const char *pc;
    char *p = const_cast<char*>(pc); // ok: but writing through p is undefinedc

    // reinterpret_cast 對其 operand 進行 low-level bit 的重新解釋
    // 要很理解其型別的 bit 組成才會使用
    int *ip;
    char *pc = reinterpret_cast<char*>(ip);
```

> cast 基本上就是擾亂型別，建議能不使用就不使用。