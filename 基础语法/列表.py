list0 = [1,2,3,4,5]
list0.sort() # 将列表从小到大排序
list0.sort(reverse=True) # 将列表从大到小排列   也可以定义 key 制定选择的元素
list0.reverse() # 将列表逆向排列
list0.pop() # 返回尾部的元素，并从原列表中删除
list0.pop(2) # 带参数则返回列表中相应下标的元素，并删除
list0.insert(0,6)
list0.append(1) # 尾部添加元素
list0.extend([9,8,7]) # 参数必须是列表[]，不能是单个元素
list0.remove(1) # 移除元素
del(list0[1]) # 删除元素
print(list0)

list0[0:5:2]
list0[10:1:-1]  #逆向选择
list0[::-1]  # 逆序 选择   不同于 reverse() 
list0[-1:-5:-2]