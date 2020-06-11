import hashlib
#密码加密 与  登陆验证
# password = '123456'
# pwlist = []
# md5 = hashlib.md5(password.encode('utf-8'))
# pwlist.append(md5.hexdigest())  # 存入加密后的密码

# pw = input('输入密码：')
# md5 = hashlib.md5(pw.encode('utf-8'))
# pw = md5.hexdigest()
# for i in pwlist:
#     if i == pw:
#         print('登录成功！')
#     else:
#         print('密码错误！')

# base64加密解密
import base64
print(base64.b64encode('我爱你'.encode('utf-8')))
print(base64.b64decode('5oiR54ix5L2g'))