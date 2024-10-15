# **登录爬虫**
## 实践简介

很多情况下，一些网站的页面或资源我们通常需要登录才能看到，但是许多网站都采取了各种各样的措施来反爬虫, 其中一种措施便是使用验证码, 常见的验证码有图片验证码, 文字点选验证码, 图标点选验证码, 滑动验证码等。

采用任意方式登录以下三个网站：

- https://login2.scrape.center/
- https://captcha8.scrape.center/
- https://captcha3.scrape.center/

## 相关概念

https://login2.scrape.center/

一个没有验证码的网站, 我们只需要输入用户名和密码即可。

https://captcha8.scrape.center/

一个有图片验证码的网站, 我们可以使用 OCR 来识别图片验证码。

https://captcha3.scrape.center/

一个有文字点选验证码的网站, 同样可以使用 OCR 来判断各个文字是否一样, 出现识别文字不一样的情况可以比较文字相似度。


## 文件说明

## 程序用途：


### selenium
selenium可以控制你的浏览器，可以实现文本填入、点击、双击、鼠标滚动、网站信息爬取、可以代替人工做一些大量且重复的工作。
## 配置环境：
本程序是在ARM架构下的macOS Ventura（版本号13.0）下进行开发。默认使用Safari浏览器【版本16.1 (18614.2.9.1.12)】进行登录爬虫。
## 配置Safari浏览器：
macOS下的Safari浏览器，需要在Safari浏览器-开发选项中打开'允许远程自动化'（如果没有运行过，则在/usr/bin/safaridriver中运行一次safaridriver程序）


## 使用方法：
分别运行三个程序即可自动登录相应网站

### 注：本实验是在ARM架构下的macOS Ventura（版本号13.0）下，使用Safari浏览器【版本16.1 (18614.2.9.1.12)】进行，若在此Windows运行本程序可能会出现错误，请对源码中的内容进行微调。

