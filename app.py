
def calculator():

    print("Calculator")

    num1 = float(input("Enter first number: "))
    op = input("Enter operator(+-*/): ")
    num2 = float(input("Enter second number: "))

    if op in "+-*/":
        print("=")
    else:
        print("")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        if num2 == 0 and op == "/":
            print("r u dum? U cant do dat")
        else:
            print(num1 / num2)
    else:
        print("Error: Invalid Operator")


def guessing_game():
    def pre_set():
        secret_word1 = "Minecraft"

        guess1 = ""
        guess_count1 = 0
        guess_limit1 = int(input("Enter the number of guesses you want: "))
        out_of_gusses1 = False

        print("")
        print("Guessing Game! You have " + str(guess_limit1) + " tries to guess the word!")

        while guess1 != secret_word1 and not (out_of_gusses1):
            if guess_count1 < guess_limit1:
                guess1 = input("Enter guess: ")
                guess_count1 += 1
            else:
                out_of_gusses1 = True

        print("")
        if out_of_gusses1:
            print("Out of Guesses, YOU LOSE! The word was: " + secret_word1)
        else:
            print("You Win!")

    def set():
        secret_word = input("What would you like the secret word to be? Enter your word: ")
        guess = ""
        guess_count = 0
        guess_limit = int(input("Enter the number of guesses you want: "))
        out_of_gusses = False

        print("")
        print("Guessing Game! You have " + str(guess_limit) + " tries to guess the word!")

        while guess != secret_word and not (out_of_gusses):
            if guess_count < guess_limit:
                guess = input("Enter guess: ")
                guess_count += 1
            else:
                out_of_gusses = True

        print("")
        if out_of_gusses:
            print("Out of Guesses, YOU LOSE! The word was: " + secret_word)
        else:
            print("You Win!")

    z = input("Would you like to choose the word? Enter Y or N: ")

    if z == "Y":
        set()
    elif z == "N":
        pre_set()
    else:
        print("Error: Invalid Option")
def guess_die():
    import random

    die_side_num = int(input("Enter the number of sides you want on your die: "))


    def roll_dice(num):
        return random.randint(1, num)


    secret_num = str((roll_dice(die_side_num)))
    guess = ""
    guess_count = 0
    guess_limit = int(input("Enter the number of guesses you want: "))
    out_of_gusses = False

    if guess_limit == 1:
        print("")
        print("Guessing Game! You have " + str(guess_limit) + " try to guess the number you rolled!")


    else:
        print("")
        print("Guessing Game! You have " + str(guess_limit) + " tries to guess the number you rolled!")

    while guess != secret_num and not (out_of_gusses):
        if guess_count < guess_limit:
            guess = input("Enter guess: ")
            guess_count += 1
        else:
            out_of_gusses = True

    print("")
    if out_of_gusses:
        print("Out of Guesses, YOU LOSE! The number was: " + secret_num)
    else:
        print("You Win! The number was: " + secret_num)
def mad_lib():
    print("Mad Lib")

    place1 = input("Enter a place: ")
    plural_noun1 = input("Enter a plural noun: ")
    adverb1 = input("Enter an adverb: ")
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb (past tense): ")
    plural_noun2 = input("Enter a plural noun: ")
    adjective2 = input("Enter an adjective: ")

    print("")
    print("This summer we went to " + place1 + " for our staycation.")
    print("We had fun riding the " + plural_noun1 + ".")
    print("The " + plural_noun1 + " went really " + adverb1 + " around the " + noun1 + ".")
    print(
        "My sister and I played " + adjective1 + " golf together, while the rest of the family " + verb1 + " with each other.")
    print("Then we ate " + plural_noun2 + ". It was " + adjective2 + ".")


def dice_game():
    import random

    print("Dice Game")

    die_side_num = int(input("Enter the number of sides you want on your die: "))


    def roll_dice(num):
        return random.randint(1, num)


    die_side_num2 = int(input("Enter the number of sides you want on your second die: "))


    def roll_dice(num):
        return random.randint(1, num)


    print("")
    print("You rolled:")
    print(roll_dice(die_side_num))
    print("&")
    print(roll_dice(die_side_num2))


def quiz():

    class Question:
        def __init__(self, prompt, answer):
            self.prompt = prompt
            self.answer = answer


    question_prompts = [
        "What is the best video game?\n(a) Fortnite\n(b) Minecraft\n(c) GTA\n(d) MarioKart\n\n",
        "What is the best fruit?\n(a) Strawberry\n(b) Blueberry\n(c) Apple\n(d) Orange\n\n",
        "What is the best movie series?\n(a) DCcomics\n(b) HarryPotter\n(c) Avengers\n(d) LOTR\n(e) PiratesOfTheCaribbean\n\n"
    ]
    questions = [
        Question(question_prompts[0], "b"),
        Question(question_prompts[1], "a"),
        Question(question_prompts[2], "c"),
    ]


    def run_test(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            print("")
            if answer == question.answer:
                score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


    run_test(questions)
def translator():
    print("What letter would you like your translator to be based on? Enter the upper and lower case versions of it.")
    upper_letter = input("Uppercase: ")
    lower_letter = input("Lowercase: ")


    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter in "aeiou":
                translation = translation + lower_letter
            elif letter in "AEIOU":
                translation = translation + upper_letter
            else:
                translation = translation + letter
        return translation


    print(translate(input("Enter a phrase: ")))

def swap_cases():
    def swap_case(s):
        translation = ""

        for letter in s:
            if letter.islower():
                translation = translation + letter.upper()
            elif letter.isupper():
                translation = translation + letter.lower()
            else:
                translation = translation + letter
        return translation


    if __name__ == '__main__':
        s = input("Enter a phrase: ")
        result = swap_case(s)
        print(result)
def cypher():
    print("Caesar Cypher")

    def translate(s):
        translation = ""
        for letter in s:
            if letter in "a":
                translation = translation + "o"
            elif letter in "b":
                translation = translation + "p"
            elif letter in "c":
                translation = translation + "q"
            elif letter in "d":
                translation = translation + "r"
            elif letter in "e":
                translation = translation + "s"
            elif letter in "f":
                translation = translation + "t"
            elif letter in "g":
                translation = translation + "u"
            elif letter in "h":
                translation = translation + "v"
            elif letter in "i":
                translation = translation + "w"
            elif letter in "j":
                translation = translation + "x"
            elif letter in "k":
                translation = translation + "y"
            elif letter in "l":
                translation = translation + "z"
            elif letter in "m":
                translation = translation + "a"
            elif letter in "n":
                translation = translation + "b"
            elif letter in "o":
                translation = translation + "c"
            elif letter in "p":
                translation = translation + "d"
            elif letter in "q":
                translation = translation + "e"
            elif letter in "r":
                translation = translation + "f"
            elif letter in "s":
                translation = translation + "g"
            elif letter in "t":
                translation = translation + "h"
            elif letter in "u":
                translation = translation + "i"
            elif letter in "v":
                translation = translation + "j"
            elif letter in "w":
                translation = translation + "k"
            elif letter in "x":
                translation = translation + "l"
            elif letter in "y":
                translation = translation + "m"
            elif letter in "z":
                translation = translation + "n"
            elif letter in "A":
                translation = translation + "O"
            elif letter in "B":
                translation = translation + "P"
            elif letter in "C":
                translation = translation + "Q"
            elif letter in "D":
                translation = translation + "R"
            elif letter in "E":
                translation = translation + "S"
            elif letter in "F":
                translation = translation + "T"
            elif letter in "G":
                translation = translation + "U"
            elif letter in "H":
                translation = translation + "V"
            elif letter in "I":
                translation = translation + "W"
            elif letter in "J":
                translation = translation + "X"
            elif letter in "K":
                translation = translation + "Y"
            elif letter in "L":
                translation = translation + "Z"
            elif letter in "M":
                translation = translation + "A"
            elif letter in "N":
                translation = translation + "B"
            elif letter in "O":
                translation = translation + "C"
            elif letter in "P":
                translation = translation + "D"
            elif letter in "Q":
                translation = translation + "E"
            elif letter in "R":
                translation = translation + "F"
            elif letter in "S":
                translation = translation + "G"
            elif letter in "T":
                translation = translation + "H"
            elif letter in "U":
                translation = translation + "I"
            elif letter in "V":
                translation = translation + "J"
            elif letter in "W":
                translation = translation + "K"
            elif letter in "X":
                translation = translation + "L"
            elif letter in "Y":
                translation = translation + "M"
            elif letter in "Z":
                translation = translation + "N"
            else:
                translation = translation + letter
        return translation

    if __name__ == '__main__':
        s = input("Enter a phrase: ")
        result = translate(s)
        print("")
        print("Translation: " + result)
def error():
    print("Error: Invalid Number")

def exit():
    print("Exited")


menu = 0


while menu != 10:
    print("")
    print("Options:")
    print("1: Calculator")
    print("2: Guessing Game")
    print("3: Guess the Number on the Die")
    print("4: Mad Lib")
    print("5: Dice Game")
    print("6: Quiz")
    print("7: Translator")
    print("8: Swap Cases")
    print("9: Caesar Cypher")
    print("10: Exit")
    print("")
    menu = int(input("What would you like to do? Enter the number: "))
    print("")
    match menu:
        case 1:
            calculator()
        case 2:
            guessing_game()
        case 3:
            guess_die()
        case 4:
            mad_lib()
        case 5:
            dice_game()
        case 6:
            quiz()
        case 7:
            translator()
        case 8:
            swap_cases()
        case 9:
            cypher()
        case 10:
            exit()
        case _:
            error()


