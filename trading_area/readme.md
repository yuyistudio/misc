Purpose 目的
============

> To get trading areas information of in a given rectangle area on the map.

获取地图上给定矩形区域内的商圈信息。

How 如何做到
===========

> Use Baidu [Map JS Api](#http://developer.baidu.com/map/reference/index.php?title=Class:%E6%9E%81%E9%80%9F%E7%89%88%E6%9C%8D%E5%8A%A1%E7%B1%BB/Geocoder) to translate a coordinate into corresponding trading areas.   

第一步，使用[百度地图的JS API](#http://developer.baidu.com/map/reference/index.php?title=Class:%E6%9E%81%E9%80%9F%E7%89%88%E6%9C%8D%E5%8A%A1%E7%B1%BB/Geocoder)将所有给定点都转换成商圈信息。
因为JS API不限制调用次数，所以使用JS API而不是Web API。

> Then use Ajax to save this information to a HTTP server. What to do next is up to you now.

第二步，将获得的信息通过Ajax传到一个HTTP服务器中保存。接下来是事情就因人而异了。

Step by step 步骤
================
```shell
python http_server.py &
```
> Start a HTTP server with the command above.

使用上述命令启动一个HTTP服务器。

> Visit `localhost:8877/static/main.html` in your browser, and click the button `start`.

使用浏览器访问网址 `localhost:8877/static/main.html`，并点击页面上的“开始”按钮。

> Visit `localhost:8877/api?action=dump` in your browser. This step will command the HTTP server to dump all the information to your disk.

在浏览器中打开`localhost:8877/api?action=dump`，这一步会将HTTP服务器中保存的信息持久化到磁盘。

```shell
python cache.py
```
> Run the command above. This command will read the information file on the disk, and print the result to the screen. You can of course redirect the output to a file.

执行上面这个命令。这个命令会从磁盘上读取内容，并打印结果到屏幕上。当然喽，你也能把输出重定向到一个文件中保存下来。

