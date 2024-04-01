
    #    can be updated using the following code also 
   

        
   
def strtodict(cs):
    for i in cs.split(';'):
        x= (i.split('='))
    # print(x)
        dictionary.update({x[0]:x[1]})
    print({x[0]:x[1] for x in[i.split('=') for i in cs.split(';')]}     )#sir^s code 

    # print(dict(x))
dictionary ={}

cs = 'a=b;c=d;e=f;g=h'

strtodict(cs)