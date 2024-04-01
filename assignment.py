def tolist(cs):
    result= []
    for i in cs.split(';'):#returns the output in a list 
        print(i)#iterating on the list 
        result.append(tuple(i.split('=')))
        print(i.split('='))
    return result
cs= "a=b;c=d;e=f;g=h"
res = tolist(cs)


