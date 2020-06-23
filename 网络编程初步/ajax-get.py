import urllib.request, urllib.parse, json

url = 'https://pagead2.googlesyndication.com/getconfig/sodar?sv=200&tid=gda&tv=r20200610&st=env'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
data = {
    'start':'10',
    'type':'T',
}
query_string = urllib.parse.urlencode(data)
url += query_string
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
txt = response.read().decode()
jt = json.loads(txt)
print(jt)
