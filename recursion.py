def factorial(n: int) -> int:
    
    if n == 1:
        return 1
    
    return n * factorial(n-1)


def fib(num):

    if num < 2:
        return num

    a = 0
    b = 1
    total = 0

    for _ in range(num-1):
        total = a+b
        a = b
        b = total
    return total

def fibonacci(num) -> int:
    
    if num < 2:
        return 1
    return fib(num-1) + fib(num-2)


print(factorial(5))   
print(fibonacci(5))