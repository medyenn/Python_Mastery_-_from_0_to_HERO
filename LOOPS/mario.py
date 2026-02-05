def main():
    square(3)


def column(height):
    print("|=|\n" * height, end="")


def row(width):
    print("|=|" * width)


def square(n):
    for _ in range(n):
        row(n)


main()
