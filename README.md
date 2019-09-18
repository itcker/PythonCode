1.使用过程中需要安装所需要的第三方库，配置相应的运行环境等

2.BeautifulSoup_urltitle_xls.py
使用BeautifulSoup实现的批量抓取url对应的title内容，同时将结果写入excel表中，此方法中的url必须同时满足以下条件：可正常访问、无指定端口、非JS生成的url和网页内容、无重定向、证书正确。需要为标准的url地址，如：https://www.baidu.com/
，不能为https://x.x.x.x:8080，

3.geturltitle.py
与BeautifulSoup_urltitle_xls.py类似，实现的批量抓取url对应的title内容以及status_code（状态码），但相比BeautifulSoup_urltitle_xls.py使用范围略广，除无法获取非JS生成的url和网页内容外，其他类型的基本可以，因代码中加入了http/https,因此只需提供简单的url即可。如：www.baidu.com或x.x.x.x:443

4.selenium_urltitle_xls.py
使用selenium+PhantomJS实现的批量抓取url对应的title内容，同时将结果写入excel表中，此方法仅适用于可正常访问的url，如：https://www.baidu.com/
无法抓取访问超时的url。另外，此方法虽为批量，但应需要调用PhantomJS，所以耗费资源，效率低，仅供参考学习，不建议批量使用

5.getiptitle.py
实现批量ip地址指定相应的端口实现web的title内容抓取

6.phantomjs.exe为浏览器，下载后放入Python的Scripts目录下，并添加到系统环境变量
