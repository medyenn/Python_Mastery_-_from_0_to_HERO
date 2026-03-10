#!/usr/bin/env python3

def main():
    height = int(input("Pyramid's Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))


if __name__ == "__main__":
    main()
