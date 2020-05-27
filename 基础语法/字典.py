girls = ['alice','bernice','clarice','aye']
boys = ['chris','arnold','bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print(letterGirls)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

s = {}
s.setdefault('a','zhao') #返回key为a的value处的指针，可进行后续操作
print(s.setdefault('b','zhao')[0])
s.setdefault('c',[]).append(10)
print(s)