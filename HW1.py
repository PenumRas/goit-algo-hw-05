def caching_fibonacci():
    cache_list = {}

    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        elif n in cache_list:
            return cache_list[n]
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)
            cache_list[n] = result
        return result

    return fibonacci


fib = caching_fibonacci()
print(fib(10))
