import random
import numpy

data = []
for i in range(30):
    num=random.randint(1,100)  # 1到100的随机数
    data.append(num)

print(data)
print(numpy.max(data))



