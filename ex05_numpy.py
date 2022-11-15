# coding=utf-8
import numpy as np

# case 多维数组
a = [1,2,3,4,5]
b = [[1, 2, 3], [ 4, 5, 6 ]]
c = np.array(b, ndmin=2)
print('a = ', a)
print('b = ', b)
print('c = ', c)
c.shape = (3,2)
print('c = ', c)

d = [[[1,2],[3,4]],[[5,6],[7,8]]]
print('d[0][0] = ', d[0][0])

# case 矩阵
e = np.matrix(d[0])
print(e)

f = np.zeros((3,4))
print('f = ', f)

g = np.ones((5,2))
print('g = ',g)

h = np.eye(4, k=1)
print('h = ', h)

i = np.identity(4)
print('i = ', i)

# case 类型转换与计算
j = [1, 2, 3, 4, 5, 6]
print('j = ', j)
k = np.asmatrix(j)
print('k = ', k)
