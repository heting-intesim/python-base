import random

print(random.random())  # 返回一个介于左闭右开[0.0, 1.0)区间的浮点数。

print(random.randint(1,10)) #产生一个1-10之间的整数，包含1 和 10 

print(random.uniform(a, b))  # 返回一个介于a和b之间（含a,b）的浮点数。如果a>b，则是b到a之间的浮点数。

print(random.randrange(start, stop[, step]))  # 返回range[start,stop)之间的一个整数，可加步长step，跟range(0,10,2)类似。

print(random.choice([1,2,3,4,5])) #随机选择列表中的一个值

print(random.normalvariate(0.3,0.1))

t = [1,2,3]
t.count