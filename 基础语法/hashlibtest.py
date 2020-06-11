
import sys
import base64
bs = base64.b64encode('宝塔镇河妖'.encode('utf-8'),)
print(bs)

sb = base64.b64decode(bs)
print(sb.decode('utf-8'))

print('宝塔镇河妖'.encode('utf-8'))

bs = base64.b64encode(s[1].encode('utf-8'))
print(bs)
