def caching_fibonacci():
    cache = {1:1, 2:1}

    def fibonacci(n):
        if n in cache.keys():
            return cache.get(n)
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return  fibonacci
res = caching_fibonacci()
print(res(5))
print(res(10))
print(res(50))
