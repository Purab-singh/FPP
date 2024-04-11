from typing import Any


class menu:
    def __init__(self):
        self.a= {}
       

    def add(self,dish,price):
        self.dish =dish
        self.price = price
        self.a.update({self.dish:self.price})
        
    def show(self):
       for i,z in  self.a.items():
           print(f"{i}:{z}")
    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            dish, price = other
            self.add(dish, price)
            return self
    def __setitem__(self, dish, price):
        self.add(dish, price)
    def __getitem__(self,dish):
        return self.a.get(dish)

    def __iter__(self):
        return iter(self.a.items())
    
    def __next__(self):
        print("in next")
        return 1
a= menu()

a.add("idly",20)    
a.add("vada",30)
a +('dosa',20) +('biryani',23)
a['sambar'] =30
print(a['idly'])
print(a.a.get("sambar"))
# a.show()
for i in a:
    print(i) 
