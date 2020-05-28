'''
1 产生随机验证码
2 用户输入验证码
3 匹配，输出提示信息
'''
import random
code = ''
letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
for i in range(4):
    code += letters[random.randint(0,len(letters)-1)]
print('验证码为：',code)
answer = input('请输入验证码（不区分大小写）：')
if answer.lower() == code.lower():
    print('输入正确')
else:
    print('输入错误')