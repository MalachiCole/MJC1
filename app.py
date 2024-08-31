# This is a comment

name_player = input("Enter Your Name: ")
menu = 0
exit_num = 20
# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *


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
        print("Welcome to the Letters to Numbers, " + name_player + "!")
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

def clock():
    clock1 = 0
    while clock1 != 1:
        print("Welcome to the Digital Clock, " + name_player + "!")
        print("A new Window has opened.")
        import tkinter as tk
        from time import strftime

        def light_theme():
            frame = tk.Frame(root, bg="white")
            frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
            lbl_1 = tk.Label(frame, font=('calibri', 40, 'bold'),
                             background='White', foreground='black')
            lbl_1.pack(anchor="s")

            def time():
                string = strftime('%I:%M:%S %p')
                lbl_1.config(text=string)
                lbl_1.after(1000, time)

            time()

        def dark_theme():
            frame = tk.Frame(root, bg="#22478a")
            frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
            lbl_2 = tk.Label(frame, font=('calibri', 40, 'bold'),
                             background='#22478a', foreground='black')
            lbl_2.pack(anchor="s")

            def time():
                string = strftime('%I:%M:%S %p')
                lbl_2.config(text=string)
                lbl_2.after(1000, time)

            time()

        root = tk.Tk()
        root.title("Digital-Clock")
        canvas = tk.Canvas(root, height=140, width=400)
        canvas.pack()

        frame = tk.Frame(root, bg='#22478a')
        frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        lbl = tk.Label(frame, font=('calibri', 40, 'bold'),
                       background='#22478a', foreground='black')
        lbl.pack(anchor="s")

        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        time()

        menubar = tk.Menu(root)
        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Light", command=light_theme)
        theme_menu.add_command(label="Dark", command=dark_theme)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        root.config(menu=menubar)
        root.mainloop()

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        clock_menu = input("What do you want to do? Enter the number: ")

        if clock_menu == "1":
            clock1 = 0
        elif clock_menu == "2":
            clock1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            clock1 = 1

def alarm():
    alarm1 = 0
    while alarm1 != 1:
        print("Welcome to the Alarm Clock, " + name_player + "!")
        print("A new Window has opened.")
        # Create Object
        root = Tk()

        # Set geometry
        root.geometry("400x200")

        # Use Threading
        def Threading():
            t1 = Thread(target=alarm)
            t1.start()

        def alarm():
            # Infinite Loop
            alarm2 = 0
            while alarm2 != 1:
                # Set Alarm
                set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

                # Wait for one seconds
                time.sleep(1)

                # Get current time
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(current_time, set_alarm_time)

                # Check whether set alarm is equal to current time or not
                if current_time == set_alarm_time:
                    print("Time to Wake up")
                    # Playing sound
                    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
                    alarm2 = 1
                    print("Please press the X in the ALARM CLOCK Window.")

        # Add Labels, Frame, Button, Optionmenus
        Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
        Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

        frame = Frame(root)
        frame.pack()

        hour = StringVar(root)
        hours = ('00', '01', '02', '03', '04', '05', '06', '07',
                 '08', '09', '10', '11', '12', '13', '14', '15',
                 '16', '17', '18', '19', '20', '21', '22', '23', '24'
                 )
        hour.set(hours[0])

        hrs = OptionMenu(frame, hour, *hours)
        hrs.pack(side=LEFT)

        minute = StringVar(root)
        minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
                   '08', '09', '10', '11', '12', '13', '14', '15',
                   '16', '17', '18', '19', '20', '21', '22', '23',
                   '24', '25', '26', '27', '28', '29', '30', '31',
                   '32', '33', '34', '35', '36', '37', '38', '39',
                   '40', '41', '42', '43', '44', '45', '46', '47',
                   '48', '49', '50', '51', '52', '53', '54', '55',
                   '56', '57', '58', '59', '60')
        minute.set(minutes[0])

        mins = OptionMenu(frame, minute, *minutes)
        mins.pack(side=LEFT)

        second = StringVar(root)
        seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
                   '08', '09', '10', '11', '12', '13', '14', '15',
                   '16', '17', '18', '19', '20', '21', '22', '23',
                   '24', '25', '26', '27', '28', '29', '30', '31',
                   '32', '33', '34', '35', '36', '37', '38', '39',
                   '40', '41', '42', '43', '44', '45', '46', '47',
                   '48', '49', '50', '51', '52', '53', '54', '55',
                   '56', '57', '58', '59', '60')
        second.set(seconds[0])

        secs = OptionMenu(frame, second, *seconds)
        secs.pack(side=LEFT)

        Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

        # Execute Tkinter
        root.mainloop()

        print("")
        print("Options")
        print("1: Play Again")
        print("2: Menu")
        alarm_menu = input("What do you want to do? Enter the number: ")

        if alarm_menu == "1":
            alarm1 = 0
        elif alarm_menu == "2":
            alarm1 = 1
        else:
            print("Error: Invalid Input")
            print("Default Procedure: Exit to Menu")
            alarm1 = 1


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
    print("17: Digital Clock")
    print("18: Alarm Clock")
    print("19: Tetris")
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
    elif menu == "17":
        clock()
    elif menu == "18":
        alarm()
    elif menu == "19":
        tetris1 = 0
        while tetris1 != 1:
            import tkinter as tk
            from tkinter import messagebox
            import random
            print("")
            print("Welcome to Tetris, " + name_player + "!")
            print("")


            print("Options")
            print("1: Easy")
            print("2: Normal")
            print("3: Hard")
            print("4: Exit")
            difficulty = input("What difficulty would you like? Enter the number: ")

            if difficulty == "1":
                width1 = 10
                height1 = 35
            elif difficulty == "2":
                width1 = 15
                height1 = 25
            elif difficulty == "3":
                width1 = 30
                height1 = 15
            elif difficulty == "4":
                tetris1 = 1
                width1 = 0
                height1 = 0
            else:
                print("Error: Invalid Input")
                print("Default Procedure: Exit to Menu")
                tetris1 = 1
                width1 = 0
                height1 = 0
            print("A new window has opened")
            print("Press the 'X' in the upper right corner to stop playing.")

            cell_size = 30
            C = width1
            R = height1
            height = R * cell_size
            width = C * cell_size

            FPS = 200

            SHAPES = {
                "O": [(-1, -1), (0, -1), (-1, 0), (0, 0)],
                "S": [(-1, 0), (0, 0), (0, -1), (1, -1)],
                "T": [(-1, 0), (0, 0), (0, -1), (1, 0)],
                "I": [(0, 1), (0, 0), (0, -1), (0, -2)],
                "L": [(-1, 0), (0, 0), (-1, -1), (-1, -2)],
                "J": [(-1, 0), (0, 0), (0, -1), (0, -2)],
                "Z": [(-1, -1), (0, -1), (0, 0), (1, 0)],
            }

            SHAPESCOLOR = {
                "O": "blue",
                "S": "red",
                "T": "yellow",
                "I": "green",
                "L": "purple",
                "J": "orange",
                "Z": "Cyan",
            }


            def draw_cell_by_cr(canvas, c, r, color="#CCCCCC", tag_kind=""):

                x0 = c * cell_size
                y0 = r * cell_size
                x1 = c * cell_size + cell_size
                y1 = r * cell_size + cell_size
                if tag_kind == "falling":
                    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2, tag=tag_kind)
                elif tag_kind == "row":
                    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2, tag="row-%s" % r)
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="white", width=2)


            def draw_board(canvas, block_list, isFirst=False):

                for ri in range(R):
                    canvas.delete("row-%s" % ri)

                for ri in range(R):
                    for ci in range(C):
                        cell_type = block_list[ri][ci]
                        if cell_type:
                            draw_cell_by_cr(canvas, ci, ri, SHAPESCOLOR[cell_type], tag_kind="row")
                        elif isFirst:
                            draw_cell_by_cr(canvas, ci, ri)


            def draw_cells(canvas, c, r, cell_list, color="#CCCCCC"):

                for cell in cell_list:
                    cell_c, cell_r = cell
                    ci = cell_c + c
                    ri = cell_r + r

                    if 0 <= c < C and 0 <= r < R:
                        draw_cell_by_cr(canvas, ci, ri, color, tag_kind="falling")


            win = tk.Tk()
            canvas = tk.Canvas(win, width=width, height=height, )
            canvas.pack()

            block_list = []
            for i in range(R):
                i_row = ['' for j in range(C)]
                block_list.append(i_row)

            draw_board(canvas, block_list, True)


            def draw_block_move(canvas, block, direction=[0, 0]):

                shape_type = block['kind']
                c, r = block['cr']
                cell_list = block['cell_list']

                canvas.delete("falling")

                dc, dr = direction
                new_c, new_r = c + dc, r + dr
                block['cr'] = [new_c, new_r]

                draw_cells(canvas, new_c, new_r, cell_list, SHAPESCOLOR[shape_type])


            def generate_new_block():

                kind = random.choice(list(SHAPES.keys()))

                cr = [C // 2, 0]
                new_block = {
                    'kind': kind,
                    'cell_list': SHAPES[kind],
                    'cr': cr
                }

                return new_block


            def check_move(block, direction=[0, 0]):

                cc, cr = block['cr']
                cell_list = block['cell_list']

                for cell in cell_list:
                    cell_c, cell_r = cell
                    c = cell_c + cc + direction[0]
                    r = cell_r + cr + direction[1]

                    if c < 0 or c >= C or r >= R:
                        return False

                    if r >= 0 and block_list[r][c]:
                        return False

                return True


            def check_row_complete(row):
                for cell in row:
                    if cell == '':
                        return False

                return True


            score = 0
            win.title("SCORES: %s" % score)


            def check_and_clear():
                has_complete_row = False
                for ri in range(len(block_list)):
                    if check_row_complete(block_list[ri]):
                        has_complete_row = True

                        if ri > 0:
                            for cur_ri in range(ri, 0, -1):
                                block_list[cur_ri] = block_list[cur_ri - 1][:]
                            block_list[0] = ['' for j in range(C)]
                        else:
                            block_list[ri] = ['' for j in range(C)]
                        global score
                        score += 10

                if has_complete_row:
                    draw_board(canvas, block_list)

                    win.title("SCORES: %s" % score)


            def save_block_to_list(block):

                canvas.delete("falling")

                shape_type = block['kind']
                cc, cr = block['cr']
                cell_list = block['cell_list']

                for cell in cell_list:
                    cell_c, cell_r = cell
                    c = cell_c + cc
                    r = cell_r + cr

                    block_list[r][c] = shape_type

                    draw_cell_by_cr(canvas, c, r, SHAPESCOLOR[shape_type], tag_kind="row")


            def horizontal_move_block(event):

                direction = [0, 0]
                if event.keysym == 'Left':
                    direction = [-1, 0]
                elif event.keysym == 'Right':
                    direction = [1, 0]
                else:
                    return

                global current_block
                if current_block is not None and check_move(current_block, direction):
                    draw_block_move(canvas, current_block, direction)


            def rotate_block(event):
                global current_block
                if current_block is None:
                    return

                cell_list = current_block['cell_list']
                rotate_list = []
                for cell in cell_list:
                    cell_c, cell_r = cell
                    rotate_cell = [cell_r, -cell_c]
                    rotate_list.append(rotate_cell)

                block_after_rotate = {
                    'kind': current_block['kind'],
                    'cell_list': rotate_list,
                    'cr': current_block['cr']
                }

                if check_move(block_after_rotate):
                    cc, cr = current_block['cr']
                    draw_cells(canvas, cc, cr, current_block['cell_list'])
                    draw_cells(canvas, cc, cr, rotate_list, SHAPESCOLOR[current_block['kind']])
                    current_block = block_after_rotate


            def land(event):
                global current_block
                if current_block is None:
                    return

                cell_list = current_block['cell_list']
                cc, cr = current_block['cr']
                min_height = R
                for cell in cell_list:
                    cell_c, cell_r = cell
                    c, r = cell_c + cc, cell_r + cr
                    if r >= 0 and block_list[r][c]:
                        return
                    h = 0
                    for ri in range(r + 1, R):
                        if block_list[ri][c]:
                            break
                        else:
                            h += 1
                    if h < min_height:
                        min_height = h

                down = [0, min_height]
                if check_move(current_block, down):
                    draw_block_move(canvas, current_block, down)



            def game_loop():
                win.update()
                global current_block, to_float
                if to_float:
                    draw_board(canvas, block_list)
                    to_float = False
                elif current_block is None:
                    new_block = generate_new_block()

                    draw_block_move(canvas, new_block)
                    current_block = new_block
                    if not check_move(current_block, [0, 0]):
                        messagebox.showinfo("Game Over!", "Your Score is %s" % score)
                        win.destroy()
                        return
                else:
                    if check_move(current_block, [0, 1]):
                        draw_block_move(canvas, current_block, [0, 1])
                    else:

                        save_block_to_list(current_block)
                        current_block = None
                        check_and_clear()
                        to_float = True

                win.after(FPS, game_loop)


            canvas.focus_set()
            canvas.bind("<KeyPress-Left>", horizontal_move_block)
            canvas.bind("<KeyPress-Right>", horizontal_move_block)
            canvas.bind("<KeyPress-Up>", rotate_block)
            canvas.bind("<KeyPress-Down>", land)

            current_block = None
            to_float = False

            win.update()
            win.after(FPS, game_loop)

            win.mainloop()
            print("Score:")
            print(score)

            print("")
            print("Options")
            print("1: Play Again")
            print("2: Menu")
            tetris_menu = input("What do you want to do? Enter the number: ")

            if tetris_menu == "1":
                tetris1 = 0
            elif tetris_menu == "2":
                tetris1 = 1
            else:
                print("Error: Invalid Input")
                print("Default Procedure: Exit to Menu")
                tetris1 = 1

    elif menu == str(exit_num):
        exit()
        menu = exit_num
    else:
        error()
