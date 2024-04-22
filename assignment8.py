class test:
    def __iter__(self):
        print("calling iter")
        return self
    def __next__(self):
        print("calling next")
        input()
        raise StopIteration
    
for i  in test():
    print(i)

class fibo:
    def __init__(self):
        self.x =0
        self.y = 1
        self.result= 0
    def __iter__(self):
        print("the number is 0\nthe number is 1")
        return self
    def __next__(self):
        self.result = self.x+self.y 
        self.x,self.y=self.y,self.x+self.y
     
        input()
        if(self.result>100):
            raise StopIteration
        return self.result
for x in fibo():
    print("the number is",x)