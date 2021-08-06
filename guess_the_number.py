import random


def run():
    random_number = random.randint(1, 100)
    chosen_number = int(input("Choose a number from 1 to 100: "))
    while chosen_number != random_number:
        if chosen_number < random_number:
            print("Chooser a greater number")
        else:
            print("Choose a smaller number")
        chosen_number = int(input("Choose another number:"))
    print("You win!")


if __name__ == "__main__":
        run()