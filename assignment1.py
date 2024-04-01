# def tolist(cs):
#     result= []
#     for i in cs.split(';'):#returns the output in a list 
#         print(i)#iterating on the list 
#         result.append(tuple(i.split('=')))
#         print(i.split('='))
#     return result
# cs= "a=b;c=d;e=f;g=h"
# res = tolist(cs)
# print(res)
res =[('a', 'b',), ('c', 'd'), ('e', 'f'), ('g', 'h')]
def tostring(res):#join function is an atribute of string not tuple not lists 
    string= ''
    for i in res:
        print(i)
        string+= '='.join(i)
        string+=';'
  
        
    print(string)
           
            # string.join('=')
            # print(i)
            # print("here")

  

tostring(res)


[('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]