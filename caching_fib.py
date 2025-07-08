FIB_REC = 'rec'
FIB_ITER = 'iter'

def rec_fibonacci(n, cache):
        if n in cache:
            return cache[n]
        
        if n <= 1:
            result = n
        else:
            result = rec_fibonacci(n - 1, cache) + rec_fibonacci(n - 2, cache)
        
        cache[n] = result
        
        return result

def iter_fibonacci(n, cache):
        if n in cache:
            return cache[n]
        
        if n <= 1:
            cache[n] = n
            return n

        max_cached_idx = max(cache.keys(), default=1)
        previous = cache.get(max_cached_idx - 1, 0)
        current = cache.get(max_cached_idx, 1)
        for i in range(max_cached_idx + 1, n + 1):
            previous, current = current, previous + current
            cache[i] = current
    
        return current

def caching_fibonacci(type = 'rec'):
    cache = {}

    match type:
        case 'rec':
            return lambda n: rec_fibonacci(n, cache)
        case 'iter':
            return lambda n: iter_fibonacci(n, cache)
        case _:
            raise ValueError("Невідомий тип обчислення. Використовуйте FIB_REC або FIB_ITER.")


if __name__ == "__main__":
    fibonacci = caching_fibonacci(FIB_ITER)
    print(fibonacci(10))
    print(fibonacci(15))
