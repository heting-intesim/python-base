girls = ['alice','bernice','clarice','aye']
boys = ['chris','arnold','bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl) # setdefault用法，当要设置的key不存在时加入，并为其赋值后一个参数；当存在key时，不进行操作，返回当前value值！
print(letterGirls)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

s = {}
s.setdefault('a','zhao') #返回key为a的value处的指针，可进行后续操作
print(s.setdefault('b','zhao')[0])
s.setdefault('c',[]).append(10)
print(s)