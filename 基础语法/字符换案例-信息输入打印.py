'''
循环提示用户输入：用户名、密码、邮箱（输入长度不超过20个，否则只有前20个有效）
用户输入q或Q时退出
格式化打印输出
'''

def get_number(char):
    """
    判断字符串中，中文的个数
    :param char: 字符串
    :return:中文字符数
    """
    count = 0
    for item in char:
        if 0x4E00 <= ord(item) <= 0x9FA5:
            count += 1
    return count

def get_space_num(s,n):
    '''
    n 实际想占有的位置数【英文】
    s 中英文混合字符串
    返回用于print的{:}占位的数
    '''
    m = get_number(s)
    return n-m


zhhs = [] #存储所有账户信息
while True:
    username = input('请输入用户名：')
    if username == 'q' or username == 'Q':
        break
    password = input('请输入密码：')
    if password == 'q' or password == 'Q':
        break
    email = input('请输入邮箱：')
    if email == 'q' or email == 'Q':
        break
    zhhs.append([username[:20], password[:20], email[:20]])

# print('用户名\t密码\t邮箱'.expandtabs(20)) #expandtabs 可将字符串中的\t转为n个空格。
print(f'{"用户名":17}{"密码":18}{"邮箱":18}') #默认字体一个汉字占2个显示位，"用户名":17实际上占位17+3=20个
for zhh in zhhs:
    # print(f'{zhh[0]}\t{zhh[1]}\t{zhh[2]}'.expandtabs(20))
    print(f'{zhh[0]:{get_space_num(zhh[0],20)}}{zhh[1]:{get_space_num(zhh[1],20)}}{zhh[2]:{get_space_num(zhh[2],20)}}')

print('end')