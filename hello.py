# asking for name
name = input("What's ur name ? ").strip().capitalize().title()
first, second = name.split(" ")
print(f"Hello, {first} {second} !", " it's nice to see you",
      "\"test separator place\"", sep=" / ", end="-_-")
print('"test prompt place"', end="-_-")
