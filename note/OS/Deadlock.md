- Deadlock

    每一種資源都有一定的instances，像是可能有五個disk，不止一個的I/O devices，每一個

    process 要利用資源都有以下三種階段
    * 要求資源
    * 使用資源
    * 釋放資源

    要死結必須要滿足以下四個條件
    1. Mutual exclusion: 一個資源一次只能被一個process所使用
    2. Hold and Wait: process取得一個資源之後等待其他的資源
    3. No preemption: 資源只能由process自己釋放，不能由其他方式釋放
    4. Circular wait: 每個process都握有另一個process請求的資源，導致每一個process都在等待另一個process釋放資源

    針對提到的死結必須滿足的條件去做預防
    Mutual exclusion: 對不可共用的資源類型而言，互斥一定成立，而可共用的資源類型，因為可以同時讀取相同檔案，所以一定不會產生。
    Hold and Wait: process必須保證一個行程在要求一項資源時，不可以佔用任何其它的資源。
    No preemption: 只要某個處理元要不到所要求的資源時，便把它已經擁有的資源釋放，然後再重新要求所要資源。
    Circular Wait: 確保循環式等候的條件不成立，我們對所有的資源型式強迫安排一個線性的順序。


- atomic

    atomic transaction
    因為一個 transaction 由一 instruction set 所組成
    如果指明了某一 transaction 是 atomic
    代表這個 transaction 在執行時, 其所屬的 instruction set 不是全部執行
    不然就是全部不執行, 沒有那種執行一半的

