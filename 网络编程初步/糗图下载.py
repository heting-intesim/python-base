# 下载出糗图 图片
import urllib.request,urllib.parse,re,os
from time import sleep

path = os.path.dirname(__file__) # 获取当前py文件的路径，用于创建文件夹存放图片
url0 = 'https://www.qiushibaike.com/imgrank/page/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
def download_img(paths):
    for i in range(len(paths)):
        request = urllib.request.Request('http:'+paths[i], headers=headers)
        urllib.request.urlretrieve('http:'+paths[i], os.path.join(path,f'/pics/{str(i)}.jpg'))
        sleep(1)

def main():
    url0 = 'https://www.qiushibaike.com/imgrank/page/'
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    start_page = int(input('start page:'))
    end_page = int(input('end page:'))
    for p in range(start_page,end_page+1):
        url = url0 + str(p)
        request = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(request)
        htmltxt = response.read().decode()
        res = re.findall(r'<div class="thumb">.*?<img src=\"(.*?)\"',htmltxt,re.S)
        download_img(res)
        # for i in range(len(res)):
        #     request = urllib.request.Request('http:'+res[i],headers=headers)
        #     response = urllib.request.urlopen(request)
        #     path_pic = os.path.join(path,f'pics\\{str(p)}_{str(i)}.jpg')
        #     with open(path_pic,'wb') as f:
        #         f.write(response.read())
        #     sleep(1)
        sleep(2) # 降低服务器负担，慢点下不影响结果
    
    print('-----------END---------')

if __name__ == "__main__":
    main()