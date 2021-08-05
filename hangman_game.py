import random
import unicodedata
import os

def read():                                                         #Read the file and extract the word as a list
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        word = unicodedata.normalize("NFD",all_lines[random.randint(1, 171)])\
            .encode("ascii", "ignore")\
            .decode("utf-8")                                        #All in one line to remove accents
        wordlist = [letter for letter in word if letter != "\n"]    #convert a word to a list
        return(wordlist)


def underscore(word):                                               #Build the undescore list from word length
    guess = ['_' for i in range(len(word))]
    return(guess)


def printing(whatever):                                             #Print a the list as a word
    for i in whatever:
        print(i, end=' ')


def comparison(choice, word, guess):                                #Compare your choice
    for i in range(len(word)):
        if guess[i] == '_':
            if choice == word[i]:
                guess[i] = choice
    return guess
    

def run():
    word = read()
    guess = underscore(word)
    while word != guess:
        os.system('clear')
        print("¡Guess the word!")
        printing(guess)
        print("\n")        
        choice = input("Type a letter")
        assert choice.isalpha(), "The input must be a letter"       #error prevention
        guess = comparison(choice, word, guess)
    os.system('clear')
    print("You win! The word is")
    printing(word)
    print("\n")


if __name__ == '__main__':
    run()