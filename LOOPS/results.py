def main():
    rank()


def rank():
    results = ["Louis", "Megan", "Travis", "Amenda"]
    print(results)
    results.append("Fred")
    print(results)

    results.append(["Laura", "Joshwa"])
    print(results)

    results.remove(["Laura", "Joshwa"])
    print(results)

    results.extend(["Laura", "Joshwa"])
    print(results)

    results.remove("Amenda")
    print(results)

    results.insert(1, "Amenda")
    print(results)

    results.reverse()
    print(results)


main()
