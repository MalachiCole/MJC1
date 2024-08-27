# This is a comment

name_player = input("Enter Your Name: ")
menu = 0
exit_num = 17


def error():
    print("Error: Invalid Input")
    print("Default Procedure: Exit to Menu")


def exit():
    print(name_player + " has left. Hope to see you here again soon!")


def calculator():
    calculator1 = 0
    while calculator1 != 1:
        print("")
        print("Welcome to the Calculator, " + name_player + "!")

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
            # I want to figure out how to make it so that if you enter a letter it will say Error: Invalid Number.
            if num2 == 0 and op == "/":
                print("r u dum? U cant do dat")
            else:
                print(num1 / num2)
        else:
            print("Error: Invalid Operator")

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        calculator_menu = input("What do you want to do? Enter the number: ")

        if calculator_menu == "1":
            calculator1 = 0
        elif calculator_menu == "2":
            calculator1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            calculator1 = 1


def guessing_game():
    guess1 = 0
    while guess1 != 1:
        print("")
        print("Welcome to the guessing game, " + name_player + "!")

        def pre_set():
            secret_word1 = "Minecraft"

            guess1 = ""
            guess_count1 = 0
            guess_limit1 = int(input("Enter the number of guesses you want: "))
            out_of_gusses1 = False

            if guess_limit1 == 1:
                print("")
                print("Guessing Game! You have " + str(guess_limit1) + " try to guess the word!")


            else:
                print("")
                print("Guessing Game! You have " + str(guess_limit1) + " tries to guess the word")

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
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            guess = ""
            guess_count = 0
            guess_limit = int(input("Enter the number of guesses you want: "))
            out_of_gusses = False

            if guess_limit == 1:
                print("")
                print("Guessing Game! You have " + str(guess_limit) + " try to guess the word")


            else:
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

        z = input("Would you like to choose the word?: ")

        if z.lower() == "y":
            set()
        elif z.lower() == "n":
            pre_set()
        elif z.lower() == "yes":
            set()
        elif z.lower() == "no":
            pre_set()
        elif z.lower() == "sure":
            set()
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        guess_menu = input("What do you want to do? Enter the number: ")

        if guess_menu == "1":
            guess1 = 0
        elif guess_menu == "2":
            guess1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            guess1 = 1


def guess_die():
    guess_die1 = 0
    while guess_die1 != 1:
        import random
        print("Welcome to Guess the Number on the Die, " + name_player + "!")
        die_side_num = int(input("Enter the number of sides you want on your die: "))

        def roll_dice(num):
            return random.randint(1, num)

        secret_num = str((roll_dice(die_side_num)))
        guess = ""
        guess_count = 0
        guess_limit = int(input("Enter the number of guesses you want: "))
        out_of_gusses = False

        # I want to figure out how to make it so that if you enter a 0 or lower or a decimal it will say Error: Invalid Number.
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

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        guess_die_menu = input("What do you want to do? Enter the number: ")

        if guess_die_menu == "1":
            guess_die1 = 0
        elif guess_die_menu == "2":
            guess_die1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            guess_die1 = 1


def mad_lib():
    mad_lib1 = 0
    while mad_lib1 != 1:
        print("")
        print("Welcome to the Mad Lib, " + name_player + "!")

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

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        mad_lib_menu = input("What do you want to do? Enter the number: ")

        if mad_lib_menu == "1":
            mad_lib1 = 0
        elif mad_lib_menu == "2":
            mad_lib1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            mad_lib1 = 1


def dice_game():
    dice_game1 = 0
    while dice_game1 != 1:
        import random
        print("")
        print("Welcome to the Dice Game, " + name_player + "!")

        # I want to figure out how to make it so that if you enter a 0 or lower or a decimal it will say Error: Invalid Number.
        die_side_num = int(input("Enter the number of sides you want on your die: "))

        def roll_dice(num):
            return random.randint(1, num)

        # I want to figure out how to make it so that if you enter a 0 or lower or a decimal it will say Error: Invalid Number.
        die_side_num2 = int(input("Enter the number of sides you want on your second die: "))

        print("")
        print("You rolled:")
        print(roll_dice(die_side_num))
        print("&")
        print(roll_dice(die_side_num2))

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        dice_game_menu = input("What do you want to do? Enter the number: ")

        if dice_game_menu == "1":
            dice_game1 = 0
        elif dice_game_menu == "2":
            dice_game1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            dice_game1 = 1


def quiz():
    quiz1 = 0
    while quiz1 != 1:
        print("")
        print("Welcome to the Quiz, " + name_player + "!")

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

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        quiz_menu = input("What do you want to do? Enter the number: ")

        if quiz_menu == "1":
            quiz1 = 0
        elif quiz_menu == "2":
            quiz1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            quiz1 = 1


def translator():
    translator1 = 0
    while translator1 != 1:
        print("")
        print("Welcome to Translator, " + name_player + "!")
        print(
            "What letter would you like your translator to be based on? Enter the upper and lower case versions of it.")
        upper_letter = input("Uppercase: ")
        lower_letter = input("Lowercase: ")

        def is_y(phrase):
            translation = ""
            for letter in phrase:
                if letter in "aeiouy":
                    translation = translation + lower_letter
                elif letter in "AEIOUY":
                    translation = translation + upper_letter
                else:
                    translation = translation + letter
            return translation

        def no_y(phrase):
            translation = ""
            for letter in phrase:
                if letter in "aeiou":
                    translation = translation + lower_letter
                elif letter in "AEIOU":
                    translation = translation + upper_letter
                else:
                    translation = translation + letter
            return translation

        y_or_no = input("Would you like to inclued y as a vowel?: ")

        if y_or_no.lower() == "y":
            print(is_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "n":
            print(no_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "yes":
            print(is_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "no":
            print(no_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "sure":
            print(is_y(input("Enter a phrase: ")))
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        translator_menu = input("What do you want to do? Enter the number: ")

        if translator_menu == "1":
            translator1 = 0
        elif translator_menu == "2":
            translator1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            translator1 = 1


def swap_cases():
    swap_cases1 = 0
    while swap_cases1 != 1:
        print("")
        print("Welcome to Swap Cases, " + name_player + "!")

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

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        swap_cases_menu = input("What do you want to do? Enter the number: ")

        if swap_cases_menu == "1":
            swap_cases1 = 0
        elif swap_cases_menu == "2":
            swap_cases1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            swap_cases1 = 1


def cypher():
    lowercase = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z")
    lowerdict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                 "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22,
                 "x": 23, "y": 24, "z": 25}
    cypher1 = 0
    while cypher1 != 1:
        print("")
        print("Welcome to the Caesar Cypher, " + name_player + "!")

        def bettertranslate(s, shift):
            translation = ""
            for letter in s:
                if letter.isalpha():
                    if letter.isupper():
                        translation = translation + (lowercase[(lowerdict[letter.lower()] + int(shift)) % 26].upper())
                    else:
                        translation = translation + (lowercase[(lowerdict[letter] + int(shift)) % 26])
                else:
                    translation = translation + letter
            return translation

        shift = input("How many times would you like to shift the cypher? Enter the number: ")

        if __name__ == '__main__':
            print("")
            s = input("Enter a phrase: ")
            result = bettertranslate(s, shift)
            print("")
            print("Translation: " + result)

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        cypher_menu = input("What do you want to do? Enter the number: ")

        if cypher_menu == "1":
            cypher1 = 0
        elif cypher_menu == "2":
            cypher1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            cypher1 = 1


def age():
    age1 = 0
    while age1 != 1:
        print("")
        print("Welcome to the Age Calculator, " + name_player + "!")
        # -*- coding: utf-8 -*-
        import time
        from calendar import isleap

        # judge the leap year
        def judge_leap_year(year):
            if isleap(year):
                return True
            else:
                return False

        # returns the number of days in each month
        def month_days(month, leap_year):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                return 31
            elif month in [4, 6, 9, 11]:
                return 30
            elif month == 2 and leap_year:
                return 29
            elif month == 2 and (not leap_year):
                return 28

        age = input("Input your age: ")
        localtime = time.localtime(time.time())

        year = int(age)
        month = year * 12 + localtime.tm_mon
        day = 0

        begin_year = int(localtime.tm_year) - year
        end_year = begin_year + year

        # calculate the days
        for y in range(begin_year, end_year):
            if (judge_leap_year(y)):
                day = day + 366
            else:
                day = day + 365

        leap_year = judge_leap_year(localtime.tm_year)
        for m in range(1, localtime.tm_mon):
            day = day + month_days(m, leap_year)

        day = day + localtime.tm_mday
        print("%s's age is %d years or " % (name_player, year), end="")
        print("%d months or %d days" % (month, day))

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        age_menu = input("What do you want to do? Enter the number: ")

        if age_menu == "1":
            age1 = 0
        elif age_menu == "2":
            age1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            age1 = 1


def leap():
    leap1 = 0
    while leap1 != 1:
        print("")
        print("Welcome to the Leap Year Tester, " + name_player + "!")
        year = int(input("Enter a year:- "))  # Here, you take the input from the user

        if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
            """
            if a year is a multiple of four and a multiple of 100 i.e. if it is a multiple of 400 it is not a leap year
            """
            print("{0} is a leap year!!".format(year))
            """
            printing the output
            """
        else:
            print("{0} is not a leap year!!".format(year))

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        leap_menu = input("What do you want to do? Enter the number: ")

        if leap_menu == "1":
            leap1 = 0
        elif leap_menu == "2":
            leap1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            leap1 = 1


def tictactoe():
    tictactoe1 = 0
    while tictactoe1 != 1:
        print("")
        print("Welcome to Tic Tac Toe, " + name_player + "! This is a 2 player game, so find a friend!")

        squares = [' '] * 9
        players = input('Enter the 2 player letters or numbers, example; XO: ')
        board = '''
          0   1   2
          {0} | {1} | {2}
         -----------
        3 {3} | {4} | {5} 5
         -----------
          {6} | {7} | {8}
          6   7   8
        '''
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]

        def check_win(player):
            for a, b, c in win_conditions:
                if {squares[a], squares[b], squares[c]} == {player}:
                    return True

        while True:
            print(board.format(*squares))
            if check_win(players[1]):
                print(f'{players[1]} is the winner!')
                break
            if ' ' not in squares:
                print('Draw!')
                break
            move = input(f'{players[0]} to move [0-8] > ')
            if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
                print('Invalid move!')
                continue
            squares[int(move)], players = players[0], players[::-1]

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        tictactoe_menu = input("What do you want to do? Enter the number: ")

        if tictactoe_menu == "1":
            tictactoe1 = 0
        elif tictactoe_menu == "2":
            tictactoe1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            tictactoe1 = 1


def oob():
    oob1 = 0
    while oob1 != 1:
        print("")
        print("Welcome to OOB, " + name_player + "!")

        def is_y(phrase):
            translation = ""
            for letter in phrase:
                if letter in "aeiouy":
                    translation = translation + "oob"
                elif letter in "AEIOUY":
                    translation = translation + "Oob"
                else:
                    translation = translation + letter
            return translation

        def no_y(phrase):
            translation = ""
            for letter in phrase:
                if letter in "aeiou":
                    translation = translation + "oob"
                elif letter in "AEIOU":
                    translation = translation + "Oob"
                else:
                    translation = translation + letter
            return translation

        y_or_no = input("Would you like to inclued y as a vowel?: ")

        if y_or_no.lower() == "y":
            print(is_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "n":
            print(no_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "yes":
            print(is_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "no":
            print(no_y(input("Enter a phrase: ")))
        elif y_or_no.lower() == "sure":
            print(is_y(input("Enter a phrase: ")))
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        oob_menu = input("What do you want to do? Enter the number: ")

        if oob_menu == "1":
            oob1 = 0
        elif oob_menu == "2":
            oob1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            oob1 = 1


def morse_code():
    morse_code1 = 0
    while morse_code1 != 1:
        print("")
        print("Welcome to the Morse Code Converter, " + name_player + "!")

        # all_the symbols
        symbols = {
            "a": ".- ",
            "b": "-... ",
            "c": "-.-. ",
            "d": "-.. ",
            "e": ". ",
            "f": "..-. ",
            "g": ".- ",
            "h": ".... ",
            "i": ".. ",
            "j": ".--- ",
            "k": "-.- ",
            "l": ".-.. ",
            "m": "-- ",
            "n": "-. ",
            "o": "--- ",
            "p": ".--. ",
            "q": "--.- ",
            "r": ".-. ",
            "s": "... ",
            "t": "- ",
            "u": "..- ",
            "v": "...- ",
            "w": ".-- ",
            "x": "-..- ",
            "y": "-.-- ",
            "z": "--.. ",
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": ".- ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            " ": "  ",
        }

        # the user has to type a word
        ask = input("Enter a phrase: ")

        length = len(ask)
        output = ""

        for i in range(length):
            if ask[i] in symbols.keys():
                output = output + " " + symbols.get(ask[i])

        print(output)

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        morse_code_menu = input("What do you want to do? Enter the number: ")

        if morse_code_menu == "1":
            morse_code1 = 0
        elif morse_code1 == "2":
            morse_code1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            morse_code1 = 1

def timer():
    timer1 = 0
    while timer1 != 1:
        print("")
        print("Welcome to the Timer, " + name_player + "!")

        import time

        def countdown(t):
            while t:
                print(t)
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1

            print('Timer completed!')

        t = input('Enter the time in seconds: ')

        countdown(int(t))

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        timer_menu = input("What do you want to do? Enter the number: ")

        if timer_menu == "1":
            timer1 = 0
        elif timer_menu == "2":
            timer1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            timer1 = 1

def l2n():
    l2n1 = 0
    while l2n1 != 1:
        def translate(s):
            translation = ""
            for letter in s:
                if letter in "a":
                    translation = translation + "1 "
                elif letter in "b":
                    translation = translation + "2 "
                elif letter in "c":
                    translation = translation + "3 "
                elif letter in "d":
                    translation = translation + "4 "
                elif letter in "e":
                    translation = translation + "5 "
                elif letter in "f":
                    translation = translation + "6 "
                elif letter in "g":
                    translation = translation + "7 "
                elif letter in "h":
                    translation = translation + "8 "
                elif letter in "i":
                    translation = translation + "9 "
                elif letter in "j":
                    translation = translation + "10 "
                elif letter in "k":
                    translation = translation + "11 "
                elif letter in "l":
                    translation = translation + "12 "
                elif letter in "m":
                    translation = translation + "13 "
                elif letter in "n":
                    translation = translation + "14 "
                elif letter in "o":
                    translation = translation + "15 "
                elif letter in "p":
                    translation = translation + "16 "
                elif letter in "q":
                    translation = translation + "17 "
                elif letter in "r":
                    translation = translation + "18 "
                elif letter in "s":
                    translation = translation + "19 "
                elif letter in "t":
                    translation = translation + "20 "
                elif letter in "u":
                    translation = translation + "21 "
                elif letter in "v":
                    translation = translation + "22 "
                elif letter in "w":
                    translation = translation + "23 "
                elif letter in "x":
                    translation = translation + "24 "
                elif letter in "y":
                    translation = translation + "25 "
                elif letter in "z":
                    translation = translation + "26 "
                elif letter in " ":
                    translation = translation + "  "
                elif letter in "A":
                    translation = translation + "1 "
                elif letter in "B":
                    translation = translation + "2 "
                elif letter in "C":
                    translation = translation + "3 "
                elif letter in "D":
                    translation = translation + "4 "
                elif letter in "E":
                    translation = translation + "5 "
                elif letter in "F":
                    translation = translation + "6 "
                elif letter in "G":
                    translation = translation + "7 "
                elif letter in "H":
                    translation = translation + "8 "
                elif letter in "I":
                    translation = translation + "9 "
                elif letter in "J":
                    translation = translation + "10 "
                elif letter in "K":
                    translation = translation + "11 "
                elif letter in "L":
                    translation = translation + "12 "
                elif letter in "M":
                    translation = translation + "13 "
                elif letter in "N":
                    translation = translation + "14 "
                elif letter in "O":
                    translation = translation + "15 "
                elif letter in "P":
                    translation = translation + "16 "
                elif letter in "Q":
                    translation = translation + "17 "
                elif letter in "E":
                    translation = translation + "18 "
                elif letter in "S":
                    translation = translation + "19 "
                elif letter in "T":
                    translation = translation + "20 "
                elif letter in "U":
                    translation = translation + "21 "
                elif letter in "V":
                    translation = translation + "22 "
                elif letter in "W":
                    translation = translation + "23 "
                elif letter in "X":
                    translation = translation + "24 "
                elif letter in "Y":
                    translation = translation + "25 "
                elif letter in "Z":
                    translation = translation + "26 "
                else:
                    translation = translation + letter
            return translation

        if __name__ == '__main__':
            s = input("Enter a phrase: ")
            result = translate(s)
            print("")
            print("Translation: " + result)

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        l2n_menu = input("What do you want to do? Enter the number: ")

        if l2n_menu == "1":
            l2n1 = 0
        elif l2n_menu == "2":
            l2n1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            l2n1 = 1

print("")
print("Welcome to the menu, " + name_player + "!")

while menu != exit_num:
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
    print("10: Age Calculator")
    print("11: Leap Year Tester")
    print("12: Tic Tac Toe")
    print("13: OOB")
    print("14: Morse Code")
    print("15: Timer")
    print("16: Letters to Numbers")
    print(str(exit_num) + ": Exit")
    print("")
    menu = input("What would you like to do? Enter the number: ")
    print("")
    if menu == "1":
        calculator()
    elif menu == "1":
        calculator()
    elif menu == "2":
        guessing_game()
    elif menu == "3":
        guess_die()
    elif menu == "4":
        mad_lib()
    elif menu == "5":
        dice_game()
    elif menu == "6":
        quiz()
    elif menu == "7":
        translator()
    elif menu == "8":
        swap_cases()
    elif menu == "9":
        cypher()
    elif menu == "10":
        age()
    elif menu == "11":
        leap()
    elif menu == "12":
        tictactoe()
    elif menu == "13":
        oob()
    elif menu == "14":
        morse_code()
    elif menu == "15":
        timer()
    elif menu == "16":
        l2n()
    elif menu == str(exit_num):
        exit()
        menu = exit_num
    else:
        error()
