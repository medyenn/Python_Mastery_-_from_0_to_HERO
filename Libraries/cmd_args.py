#!/usr/bin/env python3

import sys
# Command Line Arguments : sys.argv

# Enter your family members name after the name of the file when
# trying to run it!
if len(sys.argv) < 2:
    sys.exit("Too Few Arguments!")

print(f"Hey {sys.argv[1]} !")

for arg in sys.argv[2:]:
    print(f"{arg} is one of your family members !")
