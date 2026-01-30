
def main():
    hello()
    name = input("What's your name ? ")
    hello(name)


def hello(name = "World"):
    print(f"Hello, {name} ! \nIt's Very nce to see you !")

main()