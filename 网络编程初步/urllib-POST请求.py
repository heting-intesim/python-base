import urllib.parse
import urllib.request

post_url = 'https://fanyi.baidu.com/sug'
# 伪装请求头UA
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
# 查询数据
form_data = {
    'kw':input('请输入要查询的英文单词：'),
}
# 构建请求对象
request = urllib.request.Request(url=post_url,headers=headers)
# 处理表单数据  批量处理data数据用此方式，也可用字符串手动拼接
form_data = urllib.parse.urlencode(form_data).encode()
# form_data = 'kw=baby'.encode()
# 发送请求
response = urllib.request.urlopen(url=request,data=form_data)
print(response.read().decode())