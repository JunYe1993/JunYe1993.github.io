!['Development.jpg'](https://junye1993.github.io/image/Development.jpg)

## 讀取 Linux 的檔案資訊

Linux 的檔案有很多資訊，即使只用到檔案大小也是很方便。

## stat

- **struct stat**

    stat 的資料結構

``` C++
    #include <sys/stat.h>

    struct stat {
        dev_t     st_dev;         /* ID of device containing file */
        ino_t     st_ino;         /* Inode number */
        mode_t    st_mode;        /* File type and mode */
        nlink_t   st_nlink;       /* Number of hard links */
        uid_t     st_uid;         /* User ID of owner */
        gid_t     st_gid;         /* Group ID of owner */
        dev_t     st_rdev;        /* Device ID (if special file) */
        off_t     st_size;        /* Total size, in bytes */
        blksize_t st_blksize;     /* Block size for filesystem I/O */
        blkcnt_t  st_blocks;      /* Number of 512B blocks allocated */

        /* Since Linux 2.6, the kernel supports nanosecond
            precision for the following timestamp fields.
            For the details before Linux 2.6, see NOTES. */

        struct timespec st_atim;  /* Time of last access */
        struct timespec st_mtim;  /* Time of last modification */
        struct timespec st_ctim;  /* Time of last status change */

        #define st_atime st_atim.tv_sec      /* Backward compatibility */
        #define st_mtime st_mtim.tv_sec
        #define st_ctime st_ctim.tv_sec
    };
```

- **struct stat**

    讀取檔案 (這裡讀 .gitignore)

``` C++
    #include <stdio.h>    // for printf
    #include <time.h>     // for ctime
    #include <sys/stat.h>

    int main()
    {
        struct stat st;
        // 0 success, -1 failed
        // error code: errno
        if(stat(".gitignore", &st) == -1){
            return -1;
        }
        printf("I-node number:             %ld\n", (long) st.st_ino);
        printf("Mode:                      %lo (octal)\n", (unsigned long) st.st_mode);
        printf("Link count:                %ld\n", (long) st.st_nlink);
        printf("Ownership:                 UID=%ld   GID=%ld\n", (long) st.st_uid, (long) st.st_gid);
        printf("device containing file id: %ld\n", (long) st.st_dev);
        printf("device id:                 %ld\n", (long) st.st_rdev);
        printf("File size:                 %lld bytes\n", (long long) st.st_size);
        printf("Preferred I/O block size:  %ld bytes\n", (long) st.st_blksize);
        printf("Blocks allocated:          %lld\n", (long long) st.st_blocks);
        printf("Last status change:        %s", ctime(&st.st_ctime));
        printf("Last file access:          %s", ctime(&st.st_atime));
        printf("Last file modification:    %s", ctime(&st.st_mtime));
        return 0;
    }
```

``` bash
    I-node number:             20057552
    Mode:                      100664 (octal)
    Link count:                1
    Ownership:                 UID=1000   GID=1000
    device containing file id: 66306
    device id:                 0
    File size:                 16 bytes
    Preferred I/O block size:  4096 bytes
    Blocks allocated:          8
    Last status change:        Tue Mar 29 14:03:01 2022
    Last file access:          Sun Oct  9 19:02:52 2022
    Last file modification:    Thu Jun 17 10:20:57 2021
```

參考資料 :

1.[Linux manual page][1]

2.[程式人生][2]

[1]: https://man7.org/linux/man-pages/man2/lstat.2.html
[2]: https://www.796t.com/content/1546882764.html