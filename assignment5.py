my_lambda =lambda x:x+x
print(my_lambda(5))


my_map =map(lambda x:x**2 ,range(10))
print(list(my_map))

password = 'Hello0'
assert password =="Hello0","incorrect password"


from functools import reduce

numbers = "1,2,3,4,5"

print(reduce(lambda x,y:x+y ,numbers))

print(list(map(lambda x:x,numbers.split(','))))

