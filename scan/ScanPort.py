import re
import socket
from log.log import LogOut

logout = LogOut()

# 获取ip地址
def get_ip(target_host):
    try:
        match = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',target_host)
        if match:
            return target_host
        else:
            try:
                # 域名解析ip地址
                ip = socket.gethostbyaddr(target_host)
                return ip
            except Exception as e:
                # print('地址解析出错:',e)
                print(logout.logWaring('地址解析出错'),e)
                exit(0)
    except Exception as e:
        # print('错误1:',e)
        print(logout.logError(e),e)
        exit(0)

# 获得端口
def get_port(target_port):
    try:
        pattern = re.compile(r'(\d+)-(\d+)')
        match = re.match(pattern,target_port)
        # 获取端口如:10-8888
        if match:
            return [port for port in range(int(match.group(1)),int(match.group(2)))]
        # 获取端口如:80,3389,3306
        else:
            return [int(port) for port in target_port.split(',')]
    except Exception as e:
        # print('错误2:',e)
        print(logout.logError(e))
        exit(0)

# 扫描端口是否存在
def scanport(target_host,target_port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((target_host,target_port))
        # print('[+]{}开放端口:{}'.format(target_host,target_port))
        print(logout.logPortSuccess(target_host,target_port))
    except socket.timeout:
        pass
    except Exception as e:
        # print('错误3:',e)
        print(logout.logError(e))