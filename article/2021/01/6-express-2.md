[![](https://1.bp.blogspot.com/-AgLLG1tMStA/X45P5F8kF8I/AAAAAAAACc8/H8kNYyJT4jQH79A93yd05xr0I82-7GH7gCLcBGAsYHQ/w640-h426/Development.jpg)](https://1.bp.blogspot.com/-AgLLG1tMStA/X45P5F8kF8I/AAAAAAAACc8/H8kNYyJT4jQH79A93yd05xr0I82-7GH7gCLcBGAsYHQ/s2048/Development.jpg)

Express - Route parameters
--------------------------

 Route parameters 可以用來擷取 URL 上的 value。

*   server.js
    
            import express from 'express'
        
            // 建立 express 這 module
            var app = express()
            const port = 8888
        
            // 回傳 { "userId": xxx, "bookId": xxx }
            app.get('/users/:userId/books/:bookId', function (req, res) {
                res.send(req.params)
            })
        
            // 可以用 "-" 分割，回傳 { "userId": xxx, "authorId": xxx, "bookId": xxx }
            app.get('/users/:userId-:authorId-:bookId', function (req, res) {
                res.send(req.params)
            })
        
            // 可以用 "." 分割，回傳 { "userId": xxx, "authorId": xxx, "bookId": xxx }
            app.get('/users/:userId.:authorId.:bookId', function (req, res) {
                res.send(req.params)
            })
        
            app.get('/users', function (req, res) {
                res.send("/users\n")
            })
        
            var server = app.listen(port, function () {
                var host = server.address().address
                var port = server.address().port
                console.log("Example app listening at http://%s:%s", host, port)
            })
    
*   Testing ( [curl筆記](https://junye1993.blogspot.com/2021/01/linux-curl.html) )
    
            $ curl -X GET http://localhost:8888/users/34/books/8989
            {"userId":"34","bookId":"8989"}
        
            $ curl -X GET http://localhost:8888/users/34-789-456
            {"userId":"34","authorId":"789","bookId":"456"}
        
            $ curl -X GET http://localhost:8888/users/34.123.258
            {"userId":"34","authorId":"123","bookId":"258"}
        
            $ curl -X GET http://localhost:8888/users/
            /users
    

Express - Route handler
-----------------------

 Route handler 的 callback function 可以使用複數個，只要呼叫 next() 這個 function，便可執行下一個 callback function。

*   server.js
    
            import express from 'express'
        
            // 建立 express 這 module
            var app = express()
            const port = 8888
        
            // 可以塞複數個 callback, 只要確保你有傳和呼叫 next()
            app.get('/normal', function (req, res, next) {
                console.log('Hello from the first callback function!')
                next()
            }, function (req, res) {
                console.log('Hello from the second callback function!')
                res.send("Hi, this is the second callback function!\n")
                res.end()
            })
        
            // array 版
            function callbackA(req, res, next) {
                console.log('Hello from callbackA function!')
                next()
            }
            function callbackB(req, res, next) {
                console.log('Hello from callbackB function!')
                next()
            }
            function callbackC(req, res) {
                console.log('Hello from callbackC function!')
                res.send("Hi, this is callbackC!\n")
                res.end()
            }
        
            app.get('/array', [callbackA, callbackB, callbackC])
        
        
            var server = app.listen(port, function () {
                var host = server.address().address
                var port = server.address().port
                console.log("Example app listening at http://%s:%s", host, port)
            })
    
*   Testing - client( [curl筆記](https://junye1993.blogspot.com/2021/01/linux-curl.html) )
    
            $ curl -X GET http://localhost:8888/normal
            Hi, this is the second callback function!
            $ curl -X GET http://localhost:8888/array
            Hi, this is callbackC!
    
*   Testing - server( [curl筆記](https://junye1993.blogspot.com/2021/01/linux-curl.html) )
    
            $ node Learning/11.Express\&ES6/Route_handler.js 
            Example app listening at http://:::8888
            Hello from the first callback function!
            Hello from the second callback function!
            Hello from callbackA function!
            Hello from callbackB function!
            Hello from callbackC function!
    

參考資料 :

1\. [Express 官網](http://expressjs.com/en/guide/routing.html)