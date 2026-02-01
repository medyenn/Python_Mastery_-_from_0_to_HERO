def main():
    parity()


def compariseon():
    x = int(input("Enter the first value : "))
    y = int(input("Enter the second value : "))
    if x > y:
        print(f"The first the value {x} is greater than the second value {y} !")
    elif x < y:
        print(f"The first value {x} is less than the second value {y} !")
    else:
        print("The two values are equal")


def equity():
    x = int(input("Enter the first value : "))
    y = int(input("Enter the second value : "))
    if x != y:
        print(f"No {x} and {y} are NOT EQUAL!")
    else:
        print("Yes the two values are EQUAL!")


def grader():
    score = int(input("What is your score ? "))
    if score >= 90 and score <= 100:
        print("Your grade is : A")
    elif 80 <= score < 90:
        print("Your grade is : B")
    elif 70 <= score < 80:
        print("Your grade is : C")
    elif 60 <= score < 70:
        print("Your grade is : E")
    else:
        print("Your grade is : F")


def parity():
    x = int(input("Enter a number : "))
    if x % 2 == 0:
        print(f"The number {x} is EVEN!")
    else:
        print(f"The number {x} is ODD!")


main()
