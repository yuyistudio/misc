Purpose 目的
=======

> To get trading areas information of in a given rectangle area on the map.

获取地图上给定矩形区域内的商圈信息。

How 如何做到
===

> Use Baidu Map JS Api to translate a coordinate into corresponding trading areas.   

第一步，使用百度地图的JS API将所有给定点都转换成商圈信息。
因为JS API不限制调用次数，所以使用JS API而不是Web API。

> Then use Ajax to save this information to a HTTP server. What to do next is up to you now.

第二步，将获得的信息通过Ajax传到一个HTTP服务器中保存。接下来是事情就因人而异了。

