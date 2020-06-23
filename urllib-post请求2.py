import urllib.request, urllib.parse
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
form_data = {
    'from': 'en',
    'to': 'zh',
    'query': 'he',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '6565.326292',
    'token': '8d0a43ab31fb128fbf5d675301d99149',
    'domain': 'common',
}
headers = {
    'authority':'fanyi.baidu.com',
    'method':'POST',
    'path':'/v2transapi?from=en&to=zh',
    'scheme':'https',
    'accept':'*/*',
    # 'accept-encoding':'gzip, deflate, br',  # 取消压缩选项
    'accept-language':'zh-CN,zh;q=0.9',
    'content-length':'131',
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'BIDUPSID=743380B806F62A8FDCA79B1A476CCA43; PSTM=1575617759; BDUSS=VBwWEFyN0RtdUJJQVR4clZ2V3AzZVFMcnAtWnJ5Qktmejl-b3Vlfk9Camp4bkJlRVFBQUFBJCQAAAAAAAAAAAEAAADAn4NCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOM5SV7jOUleT; BAIDUID=743380B806F62A8FDCA79B1A476CCA43:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-233%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=31909_1461_31670_21078_31069_32046_30823_26350_22159; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1590037679,1592442266; delPer=0; PSINO=7; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1592451748; __yjsv5_shitong=1.0_7_d4addb8613a9fbae7e120b4ef4de4040868f_300_1592451966186_1.80.3.163_eade0f61; yjs_js_security_passport=c956be6b63a70264f99866323f9a5736aad94ea6_1592451967_js',
    'origin':'https//fanyi.baidu.com',
    'referer':'https//fanyi.baidu.com/',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'x-requested-with':'XMLHttpRequest',
}
form_data = urllib.parse.urlencode(form_data).encode()
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request,form_data)
with open('1.json','wb')as f:
    f.write(response.read())