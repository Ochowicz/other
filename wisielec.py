import sys

no_of_tries = 5
word = "kamila"
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

###

for _ in word:
    user_word.append("_")

while True:
    letter = input("Type a letter: ")
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("It doesn't have that letter.")
        no_of_tries -= 1
        print("Number of tries left:", no_of_tries)

        if no_of_tries == 0:
            print("End of game :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
            print(user_word)

    print("Used letters:", used_letters)
