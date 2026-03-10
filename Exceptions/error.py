#!/usr/bin/env python3


def main():
    age = get_info("what's your freaking age ??  ")
    print(f"{age}! Well.. u're not that old! Not at all !")


def get_info(prompt):
    while True:
        try:
            return (int(input(prompt)))
        except ValueError:
            pass  # This way nobody knows if I went through  an error
        # else:
        #     return age


if __name__ == "__main__":
    main()
