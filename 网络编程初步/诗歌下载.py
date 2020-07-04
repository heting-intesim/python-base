'''下载 http://www.zgshige.com/ 中国好诗网诗歌
指定第几期的 “中国好诗” 
保存诗歌名字、作者、内容，存放到html文件中
'''
import urllib.request, urllib.parse, re, time

def main():
    # f'http://www.zgshige.com/sgzk/index{_2}.shtml'
    # url_0 = 'http://www.zgshige.com/c/2020-06-19/14160928.shtml'
    url_0 = 'http://www.zgshige.com/sgzk/index_2.shtml'
    # 指定期数启示结束期
    # start_p = input('请输入起始期：')
    # end_p = input('请输入结束期：')
    # for p in range(start_p, end_p+1):
    # 实现抓取某一期的内容
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'route=8b99f870b9e93c0bc131e09a39fdc3f6; Hm_lvt_b5eef8e07365d9de6cdb271e5febbdb3=1593050191; _ga=GA1.2.251611104.1593050191; _gid=GA1.2.1731414391.1593050191; Hm_lpvt_b5eef8e07365d9de6cdb271e5febbdb3=1593051273; 122_vq=13',
        'Host': 'www.zgshige.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    request = urllib.request.Request(url_0,headers=headers)
    content = urllib.request.urlopen(request).read().decode()
    print(content)
    exit()
    # 找出诗歌title author 以及连接
    links = re.findall(r'<li>.*?<a title="(.*?)".*?href="(.*?)".*?<p class="zgshige-topauthor">(.*?)</p>',content,re.S)
    for title,link,author in links:
        request = urllib.request.Request('http://www.zgshige.com/'+link,headers=headers)
        content = urllib.request.urlopen(request).read().decode()
        text = re.findall(r'<div id="content">.*?<div class="m-lg font14 mwebfont">(.*?)</div>',content,re.S)
        text_all = f'<h1>{title}</h1><p>{author}</p>'+text[0]
        # 写入文件
        with open(r'D:/temple/shige.html','a',encoding='utf-8') as f:
            f.write(text_all)
        print(f'写完诗歌——《{title}》...')
        time.sleep(1)


if __name__ == "__main__":
    main()
