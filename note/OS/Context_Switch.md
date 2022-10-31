
當系統有多個Process時，就要進行管理，而Process Control Block (簡稱PCB)就是用來管理 Process。
毎個 Process 皆有自已的 PCB ，PCB 包含以下資訊：

Process state: Process 在哪一個狀態
Process ID
Program counter: 指明該Process下一個要執行的指令位址
CPU registers
CPU scheduling information： Process優先順序
Memory-management information
Accounting information： 用掉多少CPU的時間、使用CPU的最大時間量
I/O status information: 尚未完成的I/O Request還有哪些、還在I/O Queue中排隊之Process的編號

-   Context Switching (內容轉換)

    CPU在執行時，只能運用一個process，如果切換給另一個Process時，須將舊Process的相關資訊 (e.g.PCB內容) 儲存起來，並載入新Process的相關資訊，此過程稱『Context Switching』。

- Example

    Process A 呼叫 read() ( system call ), 進入 kernal mode, 此時有 Context Switching 改執行 Process B, 因為 Process A 進入等待直到 Disk 回復 interrupt, 再一次 Context Switching, 然後 retrun read() ( return systemcall ). Process A 回到 user mode.

- Deal with Context Switch Overhead

    Multiple Registers Set 如果只有一套 Register, 那麼新Process要載入的時候要等舊Process存會去PCB才行. 每個 Process 都有自己的 Registers Set 的話, 當 Context Switch發生時, 只要把 point 切換到另一套 Registers Set 就好

    Multithread