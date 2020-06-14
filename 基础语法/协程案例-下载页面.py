import gevent
from gevent import monkey
monkey.patch_all() # 在导入monkey后第一时间 打上补丁！！ 否则提示报警
import requests
def download(url):
    response = requests.get(url).content
    print(f'下载了{url}的数据，长度{len(response)}字节')

if __name__ == "__main__":
    urls = ['http://www.baidu.com','http://www.163.com','http://www.jd.com']
    g1 = gevent.spawn(download,urls[0])
    g2 = gevent.spawn(download,urls[1])
    g3 = gevent.spawn(download,urls[2])
    gevent.joinall([g1,g2,g3])
    print('--------END--------')