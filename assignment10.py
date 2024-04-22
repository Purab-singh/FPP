x=2
y=2
try:
    print(x)
    print(y)
except Exception as e:
    print(e)#will catch any exception
finally:
    print("hello")

number=  [1,2,3,4,5]

generor= (x **2 for x in number)
for num in generor:
    print(num)


x= {'name':1}
x.update({'age':2})
print(x['age'])
import numpy as np
x=np.array([1,2,3,4])
y=np.arange(1,10)
print(np.intersect1d(x,y))