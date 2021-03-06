from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            f'{func.__name__}({args!r}, {kwargs!r})'
            f'-> {result}'
        )
        return result
    return wrapper


@trace
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

fibonacci(4)
print(fibonacci)
