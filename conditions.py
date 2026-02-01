def main():
    x = int(input("Enter a number : "))
    if parity(x):
        print("The number is EVEN!")
    else:
        print("The number ODD!")
    revenues()


def compariseon():
    x = int(input("Enter the first value : "))
    y = int(input("Enter the second value : "))
    if x > y:
        print(f"{x} is greater than {y} !")
    elif x < y:
        print(f"{x} is less than {y} !")
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


def parity(n):
    return n % 2 == 0


def revenues():
    job = input("What is your Job title: ").strip().title()
    match job:
        case "Data Analyst" | "IT Project Manager":
            print("Average Revenue : $100k per year")
        case "Data Engineer" | "DevOps Engineer" | "Software Developer":
            print("Average Revenue : $140k per year")
        case "Data Scientist" | "Ai Engineer" | "Enterprise Architect":
            print("Average Revenue : $220k per year")
        case _:
            print("I have no idea (>^o^<)")


main()
