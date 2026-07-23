from pathlib import Path


file = Path("./meow.txt")
print(repr(file.name))
print(file.stem)
print(file.suffix)
print(file.parent)
print(repr(file.parent))
print(repr(file))  # shows that this ain't just a str but it's a platform-
#  aware object
print(file.exists())
print(file.resolve())
print(file.resolve().parent.parent.parent.name, 3 * '\n')
new_file = file.parent / ('new_' + file.stem + file.suffix)
print(repr(new_file))
