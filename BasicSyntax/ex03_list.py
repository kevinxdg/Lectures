# coding=utf-8
import numpy as np

Varname = [15.5,  21.6,  -9,  11.4,  8,  77.1]
Varname.sort()

print(np.percentile(Varname,25))


X = Varname[0]
Y=Varname[0:3]
Z=Varname[2:-1]  # [2:-1]
print('X',X)
print(Y)
print(Z)

# case 1 按规律生成序列
x = []
for i in range(1,10):
    t = i ** 2
    x = x + [t]

print(x)
print(len(x))

# case 2 序列求和
s = 0
for i in range(9):
    s = s + x[i]
print('sum of x',s)

# case 3 根据月份显示名称
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
mon = input('Input month(1--12)::')
print('mon is :', mon)
mon_index = int(mon)
print(months[mon_index-1])

#case 4 生成文件名
director = r'E:/Clouds/NutsCloud/我的坚果云/'
f = [r'fvc1.tif',r'fvc2.tif',r'fvc3.tif']

for i in [0,2,1]:
    filename = director + f[i]
    print(filename)


for item in f:
    filename = director + item
    print(filename)

#case 5 生成指定列表
nums = [0] * 10
print(nums)

nums = [i for i in range(10)]
print(nums)

nums = [i ** 2 for i in range(10)]
print(nums)

def summ(num):
    s = 0
    for i in range(1,num+1):
        s += i
    return s

nums = [ summ(i) for i in range(1,10)]
print(nums)

# case 6 查找元素
nums = [i for i in range(1,10)]
#print(nums[nums.index(5)])

# case 7 统计元素个数
nums = [1, 2, 1, 2, 1, 2, 3]
print(nums.count(1))

# For example