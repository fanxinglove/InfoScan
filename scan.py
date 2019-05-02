#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ == fanxing
# __time__ = 2019/4/23

import optparse
import threading
from multiprocessing import Pool

from scan import PingScanHost, ScanPort
from scan.BaiduSpiderDomain import BaiduSpider
from scan.FingerPrint import FingerPrint

# 获取百度的域名放入集合去重
domain = BaiduSpider()
finger = FingerPrint()

print('******************************************************')
infoscan_banner = r'''
.___        _____       _________                     
|   | _____/ ____\____ /   _____/ ____ _____    ____  
|   |/    \   __\/  _ \\_____  \_/ ___\\__  \  /    \ 
|   |   |  \  | (  <_> )        \  \___ / __ \|   |  \
|___|___|  /__|  \____/_______  /\___  >____  /___|  /
         \/                   \/     \/     \/     \/ 
'''
print(infoscan_banner)
print('******************************************************')

if __name__ == '__main__':
    usage = 'Usage:%prog -h <help>'
    parser = optparse.OptionParser(usage,version="prog v1.0")
    parser.add_option('--host',dest='target_host',type='string',help='需要扫描的IP或者域名')
    parser.add_option('--port',dest='target_port',type='string',help='需要扫描的端口，支持10-8888或80，443')
    parser.add_option('--ip',dest='target_ip',type='string',help='需要扫描的网段，支持1-255或/24')
    parser.add_option('--ping',dest='ping',type='string',default=1,help='指定扫描的方式为ping扫描')
    parser.add_option('--domain',dest='domain',type='string',help='指定domain扫描子域名')
    parser.add_option('--finger',dest='finger',type='string',help='指定finger可以进行cms指纹识别')
    options,args = parser.parse_args()
    if options.target_host != None and options.target_port != None:
        host = ScanPort.get_ip(options.target_host)
        ports = ScanPort.get_port(options.target_port)
        for port in ports:
            t = threading.Thread(target=ScanPort.scanport, args=(host, port))
            t.start()
    elif options.target_ip != None and options.ping != None:
        p = Pool(20)
        results = []
        for ip in PingScanHost.get_segment(options.target_ip):
            t = p.apply_async(PingScanHost.scannhost,args=(options.target_ip,ip))
            results.append(t)
        for t in results:
            t.get()
    elif options.target_host != None and options.domain:
        domain.spider(options.target_host)
    elif options.target_host != None and options.finger != None:
        finger.getfinger(options.target_host)
    else:
        print(parser.usage)
        exit(0)