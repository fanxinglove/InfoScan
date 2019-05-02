import time

class LogOut(object):
    # 输出端口存在的日志
    def logPortSuccess(self,target_host,target_port=''):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        logput = '[+]{} {} open port:{}'.format(current_time,target_host,target_port)
        return logput

    # 输出主机存活的日志
    def logHostSuccess(self,target_ip):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return '[+]{} Host survival:{}'.format(current_time,target_ip)

    # 输出警告错误
    def logWaring(self,output=''):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        return '[-]{} {}:'.format(current_time,output)

    # 输出致命错误
    def logError(self,output=''):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        return '[-]{} Error:{}'.format(current_time,output)