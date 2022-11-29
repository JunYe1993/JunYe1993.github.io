!['Development.jpg'](https://junye1993.github.io/image/Development.jpg)

## MD5 Intro

MD5 訊息摘要演算法（英語：MD5 Message-Digest Algorithm），一種被廣泛使用的密碼雜湊函式，可以產生出一個128位元（16個字元(BYTES)）的雜湊值（hash value），用於確保資訊傳輸完整一致。([節自wiki][1])

## 簡易 MD5 工具 : md5sum

基本上 Unix, Linux 的作業系統都有預設 md5sum

- **md5sum 用法**

``` bash
    # pipe
    $ echo "123" | md5sum
    ba1f2511fc30423bdbb183fe33f3dd0f  -

    # 讀檔
    $ md5sum .gitignore
    247bc32fd24d78844194917cb32d556a  .gitignore

    # check
    $ md5sum .gitignore > tmp.md5
    $ md5sum -c tmp.md5
    .gitignore: OK

    # pipe check
    $ echo "247bc32fd24d78844194917cb32d556a .gitignore" | md5sum -c
    .gitignore: OK
```

## openssl/evp.h

The EVP digest routines are a high level interface to message digests ([節自 Linux man page][3])。這裡註記一下 EVP 大概是代表 Envelope。雖然現在已經被改掉，但以前的 openssl/evp.h 的 #ifndef 是 HEADER_ENVELOPE_H。

- **evp 大概的流程**

``` c++
    #include <stdio.h>
    #include <string.h>
    #include <openssl/evp.h>

    int main(int argc, char *argv[])
    {
        EVP_MD_CTX *mdctx;
        const EVP_MD *md;
        char mess1[] = "Test Message\n";
        char mess2[] = "Hello World\n";
        unsigned char md_value[EVP_MAX_MD_SIZE];
        unsigned int md_len, i;

        if (argv[1] == NULL) {
            printf("Usage: mdtest digestname\n");
            exit(1);
        }

        OpenSSL_add_all_algorithms(); // 有可能有些 algo 沒有 load, ex. RSA-SHA1
        md = EVP_get_digestbyname(argv[1]);
        if (md == NULL) {
            printf("Unknown message digest %s\n", argv[1]);
            exit(1);
        }

        mdctx = EVP_MD_CTX_new();
        EVP_DigestInit_ex(mdctx, md, NULL); // _ex() 較有效率, 以前的 code 可能是 EVP_DigestInit()
        EVP_DigestUpdate(mdctx, mess1, strlen(mess1));
        EVP_DigestUpdate(mdctx, mess2, strlen(mess2));
        EVP_DigestFinal_ex(mdctx, md_value, &md_len);
        EVP_MD_CTX_free(mdctx);

        printf("Digest is: ");
        for (i = 0; i < md_len; i++)
            printf("%02x", md_value[i]);
        printf("\n");

        exit(0);
    }
```

參考資料 :

1.[MD5 wiki][1]

2.[MD5SUM wiki][2]

3.[linux man page][3]

4.[stackoverflow][4]

[1]: https://zh.wikipedia.org/wiki/MD5
[2]: https://zh.wikipedia.org/zh-tw/Md5sum
[3]: https://linux.die.net/man/3/evp_md_type
[4]: https://stackoverflow.com/questions/3055454/what-does-openssls-evp-mean
