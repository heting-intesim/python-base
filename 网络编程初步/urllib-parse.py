import urllib.parse
import urllib.request
url = 'https://www.baidu.com/s?'
word = input('请输入你想搜索的关键字：') 
data = {
    'ie':'UTF-8',
    'wd':word,
}
query_string = urllib.parse.urlencode(data) # urlencode()帮助封装字典对象。也可以将非法字符自动编码 如中文等
# response = urllib.request.urlopen(url)
# 伪装请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 构建请求对象
req = urllib.request.Request(url,headers=headers)

# 发送请求
response = urllib.request.urlopen(req)

with open(word+'.html','wb') as fp:
    fp.write(response.read())
