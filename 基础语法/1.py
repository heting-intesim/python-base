# 1——x  2——x 3——x/2 ...
def he(x):
    sum = x
    for i in range(9):
        sum += x
        x = x/2
    print(sum)

he(100)