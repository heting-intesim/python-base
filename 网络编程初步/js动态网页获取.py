from selenium import webdriver
from time import sleep
''' 尚未研究明白！！！'''
def parse_from_unicode(unicode_str):  #html DOM tree to lxml 格式
    utf8_parser = lxml.etree.HTMLParser(encoding='utf-8')
    s = unicode_str.encode('utf-8')
    return lxml.etree.fromstring(s, parser=utf8_parser)

url = 'http://www.zgshige.com/sgzk/index_2.shtml'
driver = webdriver.Chrome()
driver.get(url)
html =driver.find_element_by_name('html')
lxml_html=parse_from_unicode(html)
print(lxml_html)
# kk=lxml_html.xpath('//tr')   #使用xpath匹配


# driver.get(url)
# sleep(2)
# print(driver.page_source)
driver.close()

