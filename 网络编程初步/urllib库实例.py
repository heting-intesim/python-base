import urllib.request
# url = 'https://cg.cs.tsinghua.edu.cn/course/resource_main.htm' # 写上完整的url
# response = urllib.request.urlopen(url) # 返回一个响应对象
# print(response.read().decode('gb2312')) # 通过在网页上查看网页源代码，匆匆查看到编码方式  utf-8  gdk  gb2312....
# with open('baidu.html','wb) as f:
#     f.write(response.read())

# print(response.geturl()) # 返回请求的url
# print(dict(response.getheaders())) # 获取头部信息
# print(response.getcode())  # 获取状态码
# print(response.readlines()) # 按行读取，返回列表，字节类型

# # 下载图片
# image_url = 'https://sysware-pub.obs.cn-north-4.myhuaweicloud.com/APP/20180504140434000326cb60011a16ce49969650'
# response = urllib.request.urlopen(image_url)
# with open('1.jpg','wb') as f:
#     f.write(response.read())
# urllib.request.urlretrieve(image_url, '2.jpg')  # 直接保存url对象到本地

# 【url只能由特定的字符组成：字母、数字、下划线。  其他字符如￥中文$空格等，需要对其进行编码！】
# 【编码时使用   urllib.parse.quote()】
url = 'http://www.baidu.com/index.html?name=狗蛋&pwd=123456'
ret = urllib.parse.quote(url)  # 编码后才能提交服务器请求
re = urllib.parse.unquote(ret)  # 解码
print(ret,re,sep='\n')