import sys

# 使用 sys.argv 从命令行中传入需要的参数
list0 = sys.argv[1:]
sum = 0
for i in list0:
    sum += int(i)
print('和是：',sum)
