def fibonacci(n):
    a, b = 0, 1
    while True:
        if a > n:
            break
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)
