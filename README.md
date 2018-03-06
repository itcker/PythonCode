1.以下脚本编写环境均为Python3.6，修改及使用请注意使用对应的版本，同时在使用过程中需要安装所需要的第三库，配置相应的运行环境等，请自行百度。

2.BeautifulSoup_urltitle_xls.py
使用BeautifulSoup实现的批量抓取url对应的title内容，同时将结果写入excel表中，此方法中的url必须同时满足以下条件：1.可正常访问2.无指定端口3.非JS生成的url和网页内容4.无重定向5.证书正确。需要为标准的url地址，如：https://www.baidu.com/
，不能为https://x.x.x.x:8080，

3.geturltitle.py与BeautifulSoup_urltitle_xls.py类似，实现的批量抓取url对应的title内容，但相比BeautifulSoup_urltitle_xls.py使用范围更广，除无法获取非JS生成的url和网页内容外，其他类型的基本可以，因代码中加入了http/https,因此只需提供简单的url即可。如：www.baidu.com或x.x.x.x:443

4.selenium_urltitle_xls.py使用selenium+PhantomJS实现的批量抓取url对应的title内容，同时将结果写入excel表中，此方法仅适用于可正常访问的url，如：https://www.baidu.com/
无法抓取访问超时的url。另外，此方法虽为批量，但应需要调用PhantomJS，所以耗费资源，效率低，仅供参考学习，不建议批量使用。

6.phantomjs.exe为无头浏览器，下载后放入Python的Scripts目录下，并添加到系统环境变量

6.以上内容均为学习所写，仅供共同学习使用，大神及喷子请绕道，谢谢！
