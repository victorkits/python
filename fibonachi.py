def fibonacci(n):
    if n in (1, 2):
        return 1
    fib = fibonacci(n - 1) + fibonacci(n - 2)
    return fib



if __name__ == '__main__':
    print(fibonacci(9))

