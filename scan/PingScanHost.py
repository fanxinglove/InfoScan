import re
import subprocess
from log.log import LogOut

loging = LogOut()

# 获取要扫描的IP段
def get_segment(ip):
    # 获取IP为192.168.1.1-255
    pattern1 = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})-(\d{1,3})')
    # 获取IP为192.168.1.1/24
    pattern2 = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/(\d+)')
    match1 = pattern1.match(ip)
    match2 = pattern2.match(ip)
    if match1:
        return [int(x) for x in range(int(match1.group(1).split('.')[-1]),int(match1.group(2)))]
    elif match2:
        subnet = 32 - int(match2.group(2))
        return [int(x) for x in range(int(match2.group(1).split('.')[-1]),2**subnet)]

# 根据PING判断主机是否存在
def scannhost(ipaddrs,ip):
    ips = '.'.join(ipaddrs.split('.')[:-1]) + '.' + str(ip)
    result = subprocess.call('ping {}'.format(ips),shell=True,stdout=subprocess.PIPE)
    if result:
        pass
    else:
        print(loging.logHostSuccess(ips))