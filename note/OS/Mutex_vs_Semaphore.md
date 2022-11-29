- Semaphore

    semaphore 是作業系統中最常用的同步鎖之一。 spinlock 允許行程持續等待獲取一個鎖，相對的 semaphore 則是讓行程進入睡眠狀態，簡單來說 semaphore就是計數器，利用 up 與 down 計算擁有鎖的行程有幾個。

    semaphore中最常見的例子就是消費者與生產者問題，生產者生產商品，消費者購買商品，生產者生產商品的行為就像是 semaphore 增加，消費者購買商品就像是 semaphore減少

    ``` C++
    // <include/linux/semaphore.h>
    struct semaphore {
        raw_spinlock_t		lock;
        unsigned int		count;
        struct list_head	wait_list;
    };
    // lock ：是spinlock變量，保護 count wait_list。
    // count : 表示可以進入C.S的個數。
    // wait_list：管理在該 semaphore 上睡眠的行程，沒有獲得鎖的行程會睡眠在這個list上。
    ```

- Mutex

    在 Linux中，有種類似 semaphore的機制叫做 mutex， semaphore 在同步處理的環境中對多個處理器訪問某個分享資源進行保護的機制，mutex則適用於互斥操作。

    但若是將 semaphore的 count 設定為1，並且利用 down() 與 up() 仍然可以完成類似互斥鎖的結果，這樣為什麼要但讀實現互斥機制呢？

    因為互斥鎖的實現比較簡單與輕便，在鎖競爭激烈的測試場景中，互斥鎖比 semaphore的執行速度還要快，可擴展性更好，互斥鎖的數據結構也比semaphore還要小，所以才會單獨實現。

    ``` c++
    // <include/linux/mutex.h>
    struct mutex {
        atomic_long_t		owner;
        spinlock_t		wait_lock;
    #ifdef CONFIG_MUTEX_SPIN_ON_OWNER
        struct optimistic_spin_queue osq; /* Spinner MCS lock */
    #endif
        struct list_head	wait_list;
    };
    // count : 1代表沒有行程持有鎖，0代表有持有，負數代表有被持有且有行程在等待隊列中。
    // wait_lock ：保護 wait_list。
    // wait_list ：管理所有在mutex上的所有行程。
    // ower ：指向鎖擁有者的 task_struct。
    // osq ：用於實現MCS鎖的機制。
    ```

- Mutex vs Semaphore

    最大的差異在於 Mutex 只能由上鎖的 thread 解鎖，而 Semaphore 沒有這個限制，可以由原本的 thread 或是另外一個 thread 解開。另外，Mutex 只能讓一個 thread 進入 critical section，Semaphore 的話則可以設定要讓幾個 thread 進入。這讓實際上使用 Mutex 跟 Semaphore 場景有很大的差別。

    舉例而言，Mutex 的兩個特性：一個是隻能有持鎖人解鎖、一個是在釋放鎖之前不能退出的特性，讓 Mutex 叫常使用在 critical section 只能有一個 thread 進入，而且要避免 priority inversion 的時候；Semaphore 也能透過 binary semaphore 做到類似的事情，卻沒有辦法避免 priority inversion 出現。

    而 Semaphore 更常是用在同步兩個 thread 或功能上面，因為 Semaphore 實際上使用的是 signal 的 up 與 down，讓 Semaphore 可以變成是一種 notification 的作用，例如 A thread 執行到某個地方時 B thread 才能繼續下去，就可以使用 Semaphore 來達成這樣的作用。

- Spinlock

    基本上跟 Mutex 一樣，差異是鎖住時 waiting 方法不同

    -   Busy-waiting (Spinlock)
    在軟體工程中，忙碌等待是一種以行程反覆檢查一個條件是否為真為根本的技術，條件可能為鍵盤輸入或某個鎖是否可用。忙碌等待也可以用來產生一個任意的時間延遲，若系統沒有提供生成特定時間長度的方法，則需要用到忙碌等待。不同的電腦處理器速度差異很大，特別是一些處理器設計為可能根據外部因素動態調整速率。


    -   Sleep-waiting (Mutex)
    維基百科上並沒有對 Sleep-waiting 做介紹，所以筆者用更簡單的例子說明:
    假設我們今天在湯X熊遊樂場，當 A 機台已經有兩個小朋友占用，如果以 Busy-waiting 的方法來看，我們會傻傻的站著等到小朋友玩夠了，才換我們上去玩。而 Sleep-waiting 則是讓我們先去做其他事情，等到小朋友玩夠了再通知我們過去玩。