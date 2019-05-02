import requests
import json
from lib.headers import GetHeader

headers = GetHeader.header

class FingerPrint:
    def __init__(self):
        self.url = 'http://whatweb.bugscaner.com/what.go'
        self.headers = {'User-Agent':headers}

    # 利用bugscanner在线指纹识别
    def getfinger(self,domain):
        data = {
            'url':domain,'location_capcha':'on'
        }
        response = requests.post(url=self.url,headers=self.headers,data=data).text
        content = json.loads(response)
        try:
            print('+---------+------------------+')
            print('|   CMS   | {} '.format(content['CMS']))
            print('+---------+------------------+')
            try:
                print('|Languages| {} '.format(content['Programming Languages']))
                print('+---------+------------------+')
            except KeyError:
                content['Programming Languages'] = '未知'
                print('|Languages| {} '.format(content['Programming Languages']))
                print('+---------+------------------+')

            try:
                print('|WebServer| {} '.format(content['Web Servers']))
                print('+---------+------------------+')
            except KeyError:
                content['Web Servers'] = '未知'
                print('|WebServer| {} '.format(content['Web Servers']))
                print('+---------+------------------+')

            try:
                print('|Framework| {} '.format(content['JavaScript Frameworks']))
            except KeyError:
                content['JavaScript Frameworks'] = '未知'
                print('|Framework| {} '.format(content['JavaScript Frameworks']))
            print('+---------+------------------+')
        except KeyError:
            print('[-]请刷新whatweb.bugscaner.com验证码')