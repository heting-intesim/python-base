import urllib.request, urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
post_data = {
    'cname': '西安',
    'pid': '',
    'pageIndex': '1',
    'pageSize': '50',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
data = urllib.parse.urlencode(post_data).encode()
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request,data=data)
print(response.read().decode())