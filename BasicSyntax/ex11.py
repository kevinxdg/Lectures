
# 这是一段注释说明
# 这段代码的功能是。。。。

# python 基础语法： 变量和运算

# 赋值

x = 3.1415926
s = '姓名'
b = True
c = False
c = True

# 数据运算
pi = 3.1415926
r = 2
S = pi * r * r



s = "这个圆面积是：%f--------" % S

print(S)
print(s)

# 逻辑运算 与 或  非
b = True
c = True
d = False
e = b and d  # 与运算 两个true 结果 true
f = b or d  # 或运算 只要有一个true，结果就是true
print(e)
print(f)

# 比较运算 结果 逻辑值
# > < == != >= <=
print((pi >= 3.14) and (pi <= 3.15))      # 3.14<=pi<=3.15 是否成立

# 语法结构
# 条件语句结构

if pi >= 3.15:
    print('pi > ')
else:
    print('pi < ')

score = 85
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('中等')
else:
    print('差')


# 循环结构

for i in range(3):
    for j in range(3):
        print("(%d, %d)"%(i,j))
print('----------------------------')
for i in range(2, 10):
    print('*' * i)

for i in range(41):
    if i * 2 + (40-i) * 4 == 100:
        print('鸡：%d 兔：%d' % (i, 40-i))


# 定义函数

# def 函数名（参数）:
#     代码
#     return 返回值

def assess(score):
    if score >= 90:
        print('优秀')
    elif score >= 80:
        print('良好')
    elif score >= 60:
        print('中等')
    else:
        print('差')

assess(89)
assess(98)
assess(65)

def chicken_rabbit(head, feet):
    # i 鸡的数量
    for chicken in range(head+1):
        print('in function: %d' % chicken)
        rabbit = head - chicken
        if chicken * 2 + rabbit * 4 == feet:
            return chicken
    return "无解"

solve = chicken_rabbit(42,98)
print(solve)

import numpy as np

x = 101.56
y = np.power(x, 3.1)
y1 = np.log(x)
print(y1)

print('aaa')
print(r'\n')
print('bbb')