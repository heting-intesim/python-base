import re,urllib.request
content = '''
<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHanq' ess-data='https://www.privacypic.com/images/2020/05/30/uNHanq.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHtoU' ess-data='https://www.privacypic.com/images/2020/05/30/uNHtoU.jpg'>&nbsp;<br>脸蛋还是蛮可爱的，有兴趣的朋友可以留言或私信，补发农家乐美女图。<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNH7YZ' ess-data='https://www.privacypic.com/images/2020/05/30/uNH7YZ.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNH8T6' ess-data='https://www.privacypic.com/images/2020/05/30/uNH8T6.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHpC0' ess-data='https://www.privacypic.com/images/2020/05/30/uNHpC0.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHYkn' ess-data='https://www.privacypic.com/images/2020/05/30/uNHYkn.jpg'>&nbsp;<br>后来终于说服拍不露面的自拍，看着照片里的骚屁股，又硬起来了。<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHHa9' ess-data='https://www.privacypic.com/images/2020/05/30/uNHHa9.jpg'>&nbsp;<br>人妻就是胸大屁股圆哈，苹果前置的像素渣的可怜<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHEv3' ess-data='https://www.privacypic.com/images/2020/05/30/uNHEv3.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHfih' ess-data='https://www.privacypic.com/images/2020/05/30/uNHfih.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHPuH' ess-data='https://www.privacypic.com/images/2020/05/30/uNHPuH.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHnUJ' ess-data='https://www.privacypic.com/images/2020/05/30/uNHnUJ.jpg'>&nbsp;<br>中途干着的时候，七七老公打电话过来，可惜没接，要是接了，一边和老公打电话，一边操逼是太爽了。<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNOMYa' ess-data='https://www.privacypic.com/images/2020/05/30/uNOMYa.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNHwn7' ess-data='https://www.privacypic.com/images/2020/05/30/uNHwn7.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNOlCy' ess-data='https://www.privacypic.com/images/2020/05/30/uNOlCy.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNO0QR' ess-data='https://www.privacypic.com/images/2020/05/30/uNO0QR.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNOxmV' ess-data='https://www.privacypic.com/images/2020/05/30/uNOxmV.jpg'>&nbsp;<br>干完两炮，准备和七七出去吃个饭，趁着穿衣服偷拍两张。<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNOGyu' ess-data='https://www.privacypic.com/images/2020/05/30/uNOGyu.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNOLag' ess-data='https://www.privacypic.com/images/2020/05/30/uNOLag.jpg'>&nbsp;<br>这胸36C，你们觉得呢？<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNOkqF' ess-data='https://www.privacypic.com/images/2020/05/30/uNOkqF.jpg'>&nbsp;<br><img cs-data='http://a.0ad/bl0ck.jpg' data-link='https://www.privacypic.com/image/uNOSxz' ess-data='https://www.privacypic.com/images/2020/05/30/uNOSxz.jpg'>&nbsp;<br>
'''
#  ess-data='https://www.privacypic.com/images/2020/05/30/uNHanq.jpg'
res = re.findall(r'ess-data=\'(.*?)\'',content)
headers = {
    'authority': 'cl.vaakc.com',
    'method': 'GET',
    'path': '/htm_data/2006/16/3949486.html',
    'scheme': 'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # accept-encoding: 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d7407efc592946894b1cbd66aa68dc1c81591772470; 227c9_lastvisit=0%091591866045%09%2Fread.php%3Ftid%3D3964123',
    # 'if-modified-since': 'Mon, 15 Jun 2020 06:57:21 GMT',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}
# request = urllib.request.Request(url=url,headers=headers)
for i in range(len(res)):
    request = urllib.request.Request(url=res[i],headers=headers)
    response = urllib.request.urlopen(request)
    with open(f'{i}.jpg','wb') as f:
        f.write(response.read())