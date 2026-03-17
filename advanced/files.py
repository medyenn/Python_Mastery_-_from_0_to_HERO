password = input("enter your password: ")

# In the case above, we write to the file
# But since we used the mode Write "w", we will override the file everytime
# we run the file and enter a new password :
# file = open("helper.txt", "w")
# file.write(f"the previous one is overriden\nnew: {password}")
# file.close()


# But this time we will choose the mode : APPEND ("a")
# This way we can save the file data the way it is and append the
# the new data at the end of the file everytime we run the program
file = open("helper1.txt", "a")
file.write(f"{password}\n")
file.close()

# In the previous cases we had to close the file manually so if we don't
# close it ourselves it's gonna remain open, But the good news:
# there is the CONTEXT MANAGERS who manage to close any sort of resource
# automatically once we're done with it

with open("helper1.txt", "a") as file:
    file.write("This time we don't need to close it manually!\n")

print("\n== Now we will read from a file ==\n")
with open("first_generator.py", "r") as file:
    lines = file.readlines()
    for i in range(5):
        print(lines[i].rstrip())
print("\n== Now we read from another file! ==\n")
with open("helper2.txt", "r") as file:
    for line in file:
        print(line.rstrip())

print("\n== Now we try to apply some operations on what we read ==\n")
people = []
with open("helper2.txt") as file:
    # When we only need to read from a file, then we don't need to specify
    # the mode "r", it's always "r" by default untill we enter a different mode
    for line in file:
        people.append(line[:8].rstrip().upper())

print(sorted(people))

people = {}
# Now we will take the file data sorted:
with open("helper2.txt") as file:
    for line in sorted(file):
        name, state = line.split(',')
        print(f'{name.rstrip().title()} from {state.rstrip().title()}')

# In the previous two exaples we had to format the file's data in a specific
# format so that we can apply these ops on it and still get a valid output
# Because we had two categories of data
# So In such cases we have a better solution, which is when we have different
# Categories of data that kind of relate we can organize them in a "csv" file :
with open("helper2.csv") as file:
    for line in file:
        ...
