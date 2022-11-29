-   TCP

    The transmission control protocol (TCP) is defined as a connection-oriented communication protocol that allows computing devices and applications to send data via a network and verify its delivery, forming one of the crucial pillars of the global internet.

    TCP relies on a three-way handshake (synchronization, synchronization acknowledgment, and final acknowledgment)

    Before one can send any data, the client and server must establish a connection. The server must actively listen for client requests whenever a connection is established. The TCP protocol is connection-based, so it creates and maintains a connection between the receiver and the sender while the data is being passed between them. Therefore, any information that travels through the internet is guaranteed to arrive unaltered.

    1. The client confirms data delivery from the server.
    2. After a timeout period, the server attempts retransmission for data that is not delivered.
    3. In a congested network, TCP delays data transmission.
    4. It uses a three-way handshake to check for data transmission errors.

- UDP

    What is distinctive about UDP is that it is not connection-based. In this case, “connectionless” refers to the fact that no connection is established before communication occurs.

    The UDP protocol is not suitable for sending electronic mail, viewing a web page, or downloading a file. However, it is preferred mainly for real-time applications like broadcasting or multitasking network traffic. UDP’s key features are as follows:

    1. It adapts to bandwidth-intensive applications that tolerate a loss of packets.
    2. There will be fewer delays in data transmission.
    3. It is used to send a large number of packets at a time.
    4. There is a possibility that you may lose some data.

- Differences.

    1. TCP is connection-oriented while UDP is connectionless
        -   UDP is a connectionless protocol. This type of data transmission involves an endpoint of a network sending an IT signal without checking whether a receiver is available or available to receive the signal.

    2. TCP leverages more error-checking mechanisms than UDP
        -   Restraining the connection after a timeout period
        -   Including a checksum field in the header
        -   Sending and receiving acknowledgments

    3. TCP sends data in a particular sequence, whereas there is no fixed order for UDP protocol

    4. UDP is faster and more efficient than TCP

    5. Unlike UDP, TCP cannot be used for multicast or broadcast services
        -   Internet Control Message Protocol

    6. TCP leverages flow control, while UDP does not

    7. UDP does not control congestion, whereas TCP implements congestion avoidance algorithms

    8. TCP is more reliable than UDP

    9. The TCP header is different from the UDP header

    10. UDP is suitable for live and real-time data transmission, which TCP cannot support
