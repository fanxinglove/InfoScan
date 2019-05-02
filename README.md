# InfoScan

信息收集，功能有子域名采集，端口扫描，存活主机，cms指纹识别。

# 安装与环境

环境：python3

安装模块：requests,bs4

# 使用

##### 帮助文档

`python3 scan.py -h`

![](https://raw.githubusercontent.com/fanxinglove/InfoScan/master/images/1.png)

##### 子域名采集

`python3 scan.py --host=www.xxx.com --domain=1`

##### 端口扫描

`python3 scan.py --host=192.168.1.45 --port=80,443,3389`

`python3 scan.py --host=192.168.1.45 --port=80-200`

##### 存活主机

`python3 scan.py --ip=192.168.1.1/24`

##### CMS指纹识别

`python3 scan.py --host=www.scitc.com.cn --finger=1`

