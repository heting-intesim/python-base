import urllib.request
url = 'https://cl.vaakc.com/htm_data/2006/16/3949486.html'
headers = {
    'authority': 'cl.vaakc.com',
    'method': 'GET',
    'path': '/htm_data/2006/16/3949486.html',
    'scheme': 'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # accept-encoding: 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d7407efc592946894b1cbd66aa68dc1c81591772470; 227c9_lastvisit=0%091591866045%09%2Fread.php%3Ftid%3D3964123',
    # 'if-modified-since': 'Mon, 15 Jun 2020 06:57:21 GMT',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('gbk')

import re
res = re.findall(r'https://[.*?].jpg',content)
print(res)