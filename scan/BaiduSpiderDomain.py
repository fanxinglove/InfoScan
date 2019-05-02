import re
import time
import random
import requests
from bs4 import BeautifulSoup
from lib.headers import GetHeader

headers = GetHeader.header

def get_host(target_host):
    pattern = re.compile('www.(.*)')
    get_url = re.search(pattern,target_host)
    if get_url:
        return get_url.group(1)
    else:
        return target_host

class BaiduSpider:
    def __init__(self):
        self.url = 'https://www.baidu.com/s?wd=site:{}&pn={}'
        self.headers = {'User-Agent':headers}
        self.args = set()

    # 爬取百度的5页
    def spider(self,target_host):
        target_host = get_host(target_host)
        print('[*]正在爬取子域名，请等待...')
        for i in range(5):
            try:
                response = requests.get(url=self.url.format(target_host,str(i*10)),headers=self.headers).text
                soup = BeautifulSoup(response,'lxml')
                results = soup.find_all(name='a',attrs={'data-click':re.compile(('.*')),'class':None})
                for result in results:
                    result = result.get('href')
                    result = requests.get(url=result,headers=self.headers,timeout=3).url
                    pattern = re.compile(r'http://(.*?)/.*?')
                    domain_url = re.search(pattern,result).group(1)
                    # print(domain_url)
                    self.args.add(domain_url)
                time.sleep(random.randint(2,4))
            except Exception:
                pass
        print('+--------------------+')
        print('|子 域 名 采 集 列 表|')
        print('+--------------------+')
        for domain in self.args:
            print('|{}'.format(domain))
            print('+--------------------+')
