def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    x = 10
    for n in fibonacci_gen(x):
        print(n, end=' ')

    print()

    x = fibonacci_gen(10)
    for _ in range(10):
        print(next(x), end=' ')


main()
