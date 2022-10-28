
- Proces vs Thread

    Process 等於已經被放進(load)記憶體內, 並執行的 Program(程式碼).
    Process 由 Memery Space 和 一個以上的 Thread 組成, 每一個 Process 互相獨立

    ```
    每個 Process 所需的記憶體總合，也可能大於實體記憶體，因此需要用次級儲存裝置充當虛擬記憶體 (Virtual Memory)，因此如何對虛擬記憶體做到最小的依賴，盡可能避免 Page Fault，並防止 Thrashing 的發生以達到最佳化，也是作業系統 (OS) 需要處理的學問。
    ```

    Process 是 Thread 的容器, 也就是一個 Process 能有多個 Thread.
    Thread 是系統處理工作的基本單元, 一個 Process 底下的 Thread 共享資源，如記憶體、全域變數.
    但這些 Thread 各自擁有其 Stack, 等於是 local variable 各自獨立.

    ```
    在多執行緒中 (Multithreading)，兩個執行緒若同時存取或改變全域變數 (Global Variable)，可能會發生同步 (Synchronization) 問題。若執行緒之間互搶資源，則可能產生死結 (Deadlock)，如何避免 (Prevent) 或預防 (Avoid) 上述兩種情況的發生，仍是作業系統 (OS) 所關注的
    1.這個資源不能同時給兩個人用。
    2.有一個人拿了一個資源，又想拿別人的資源。
    3.如果一個人占用資源很久，仍不能趕他走。
    4.A 等 B，B 等 C，C 等 D，D 又等 A，等成一圈。
    ```

    ```
    Both processes and threads are independent sequences of execution. The typical difference is that threads (of the same process) run in a shared memory space, while processes run in separate memory spaces.

    I'm not sure what "hardware" vs "software" threads you might be referring to. Threads are an operating environment feature, rather than a CPU feature (though the CPU typically has operations that make threads efficient).

    Erlang uses the term "process" because it does not expose a shared-memory multiprogramming model. Calling them "threads" would imply that they have shared memory.
    ```