# While loop
i = 0
while i < 2:
    print("'i' is still less than 2 !")
    i += 1

# for loop
for _ in range(2):
    print("I prefer this one!")

# printing loops :
print("This one is easier but less readable somtimes!\n" * 2, end="")

# example :
name = input("Enter Your Name : ").strip().title()
while True:
    i = int(input("Enter how many times you want it printed: "))
    if i > 0:
        break

for _ in range(i):
    print(name)
