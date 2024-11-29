
for i in range(10):
    print(i)

def add1(x):
    return (x**2+1)

a = add1(100)
print(a)


sname = r'1980-02-03'
sname = r'1980-%02d-%2d' % (12,3)
print(sname)