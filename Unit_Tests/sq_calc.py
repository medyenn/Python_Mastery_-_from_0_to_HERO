def main():
    x = int(input("x: "))
    print(ft_square(x))


def ft_square(x):
    # I made this error on purpose in order to see how we test bugs
    return x**2


def ft_hello(to='World'):
    print("Hello,", to)


def ft_helo(to='World'):
    return f'Hello, {to}'


if __name__ == '__main__':
    main()