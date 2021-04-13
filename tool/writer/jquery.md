!['ProgrammerLife.jpg'](https://junye1993.github.io/image/ProgrammerLife.jpg)

## JQuery - $( document ).ready()

鑒於 $( document ).ready() 有縮寫，導致初學者如我看不懂，這裡紀錄一下。

- **基本版本**

    $( document ).ready() 基本上是等 Document Object Model ( DOM ) 好了後，可以執行 JavaScript code 時啟動。另外常見的 $( window ).on( "load", function() { ... }) 則是等整個文件都處理完畢後 ( 包含 image, iframe...等等 ) 才執行，而非只有 DOM。

``` javascript
    // A $( document ).ready() block.
    $( document ).ready(function() {
        console.log( "ready!" );
    });
```

- **縮寫版本**

    老練的開發者會寫 $() 代替 $( document ).ready()，但最好不要。

``` javascript
    // Shorthand for $( document ).ready()
    $(function() {
        console.log( "ready!" );
    });
```

參考資料 :

1.[JQuery_Doc](https://learn.jquery.com/using-jquery-core/document-ready/)