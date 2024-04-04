def is_leap_year(year):
    match year % 4:
        case 0:
            match year % 100:
                case 0:
                    match year % 400:
                        case 0:
                            return True  # Divisible by 400
                        case _:
                            return False  # Divisible by 100 but not 400
                case _:
                    return True  # Divisible by 4 but not by 100
        case _:
            return False  # Not divisible by 4
print(is_leap_year(2001))
            
a=10
def legb_rule():
    a=2
    def encodeing():
        print(a)
        print(print)
    return encodeing
x= legb_rule()
x()
legb_rule()
print(a)


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


