#!/usr/bin/env python3

import logging

values = [-23, 0, 5]

for value in values:
    try:
        print(int(100 / value))
    except ZeroDivisionError:
        pass

print()

values = [0, -146, 0]

for value in values:
    try:
        print(int(1000 / int(value)), end=" ")
    except ZeroDivisionError:
        continue
    print("[OK]")


print()

values = ["ok", 0, -11, 5]

for value in values:
    try:
        print(int(100 / value))

    except (ZeroDivisionError, TypeError) as e:
        print(str(e), e, e.__format__,  sep="\n")
        print("\nOK")
    except ValueError:
        pass

    except Exception as e:
        print(e)
        logging.exception(e)
    finally:
        print("We're Fine!\n")
        continue
