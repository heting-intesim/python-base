from bs4 import BeautifulSoup

# 生产对象
soup = BeautifulSoup(open('soup.html',encoding='utf8'), 'lxml') # 返回一个BeautifulSoup对象
# print(soup.div) # 只能找到第一个符合要求的标签
# print(soup.a['href']) # 没有标签则返回None,返回对应属性
# print(soup.a.attrs) # 返回标签内所有属性

# print(soup.a.text) # 获取内容
# print(soup.a.string) # 获取内容 ,只能获取纯文字
# print(soup.a.get_text()) # 获取内容

# print(soup.find('a'))
# print(soup.find('a',title="163")) # 第二个参数筛选
# print(soup.find('div',class_="tang")) # 使用class时需要加下划线

# div = soup.find('div', class_="tang")
# print(div.find('a',title="jd"))

# # find_all()方法
# print(soup.find_all('a')) # 返回全文符合要求的所有对象列表

# print(soup.find_all(['a','b']))
# print(soup.find_all('a',limit=2)) # 限制找回的个数

print(soup.select('#jing')[0].text) # id
print(soup.select('.tang')) # class