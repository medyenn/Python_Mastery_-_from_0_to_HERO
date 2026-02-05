def main():
    spell_game()


def spell_game():
    words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}
    print("Welcome to spelling Bee!\nLetters : A I P C R H G")
    while len(words) > 0:
        print(f"===============\nYou need to extract {len(words)} words!")
        guess = input("Guess a word : ").strip().upper()
        if guess == "GRAPHIC":
            words.clear()  # .clear() dictionary method
            print("|=====> This is the *MAGIC* word! You've Won! <=====|")

        elif guess in words.keys():
            point = words.pop(guess)   # .pop() dictionary method
            print(f"Good Job! you scored {point} points!")
        else:
            print("Try Again !")

    words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

    final = input("\nDo you want to see the words and their worth?\n\
            (yes/no) : ").strip().lower()
    if final == "yes":
        for word, score in words.items():   # .items() dictionary method
            print(f"{word}\t: was worth {score} points.")


main()
