!['ProgrammerLife.jpg'](https://junye1993.github.io/image/ProgrammerLife.jpg)
## stack v.s. heap

- **與 threads 的互動**

    在一個 multi-threaded 的程式中，每個 thread 都各自擁有一個 stack，但共享一個 heap。
  
- **object 可以儲存在 heap，而非 stack**

    在 c++ 可以使用 new，來將 object 實體儲存在 heap。
``` c++
    void foo () {
        // myClass, myPointer 儲存在 stack
        // myPointer 所指向的 tempClass object 則儲存在 heap
        // function 結束 myClass, myPointer 則會與 stack 一起 remove
        // 而 myPointer 所指向的 tempClass 不會，所以下 delete
        tempClass myClass;
        tempClass *myPointer = new tempClass();
        delete myPointer;
    }
```
- **stack 跟 heap 的大小**

    stack 大小是固定的，有某些語言可以增加其大小。若 stack 不夠則會造成 stackoverflow (ex 無限遞迴)。heap 大小則是靠 OS 給的。

參考資料 :

1.[difference-between-stack-and-heap](http://www.programmerinterview.com/data-structures/difference-between-stack-and-heap/)