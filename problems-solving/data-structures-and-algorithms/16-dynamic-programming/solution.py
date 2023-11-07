def solution_1(n, cache={}):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = solution_1(n - 1, cache) + solution_1(n - 2, cache)
    return cache[n]


def solution_2(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b
