x = float(input("Enter the first value : "))
y = float(input("Enter the second value : "))

z = round(x + y)

print(f"{z:,}")
z = round(x / y, 2)
print(z)

z = x / y
print(f"{z:.2f}")


def main():
    x = int(input("enter the number to be squared :"))
    print(f"{x} squared is :", square(x))


def square(n):
    return n * n


main()
