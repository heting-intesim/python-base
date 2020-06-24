'''下载 http://www.zgshige.com/ 中国好诗网诗歌
指定第几期的 “中国好诗” 
保存诗歌名字、作者、内容，存放到html文件中
'''
import urllib.request, urllib.parse, re, time

def main():
    # f'http://www.zgshige.com/sgzk/index{_2}.shtml'
    url_0 = 'http://www.zgshige.com/c/2020-06-19/14160928.shtml'
    # 指定期数启示结束期
    # start_p = input('请输入起始期：')
    # end_p = input('请输入结束期：')
    # for p in range(start_p, end_p+1):
    # 实现抓取某一期的内容
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    request = urllib.request.Request(url_0,headers=headers)
    content = urllib.request.urlopen(request).read().decode()
    # print(content)
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
