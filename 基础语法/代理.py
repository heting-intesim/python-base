import urllib.request,urllib.parse

# 高级功能首先创建handler
handler = urllib.request.ProxyHandler({'http':'163.125.223.102:8088',}) # 此处写入可用的代理服务器ip信息
# 创建opener
opener = urllib.request.build_opener(handler)

url = 'https://www.baidu.com/s?ie=UTF-8&wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
}
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
with open('1.html','wb') as f:
    f.write(response.read())