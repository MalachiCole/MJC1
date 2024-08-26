name_player = input("Enter Your Name: ")

cypher1 = 0
while cypher1 != 1:
    print("")
    print("Welcome to the Caesar Cypher, " + name_player + "!")


    def shift1():
        def translate(s):
            translation = ""
            for letter in s:
                if letter in "a":
                    translation = translation + "b"
                elif letter in "b":
                    translation = translation + "c"
                elif letter in "c":
                    translation = translation + "d"
                elif letter in "d":
                    translation = translation + "e"
                elif letter in "e":
                    translation = translation + "f"
                elif letter in "f":
                    translation = translation + "g"
                elif letter in "g":
                    translation = translation + "h"
                elif letter in "h":
                    translation = translation + "i"
                elif letter in "i":
                    translation = translation + "j"
                elif letter in "j":
                    translation = translation + "k"
                elif letter in "k":
                    translation = translation + "l"
                elif letter in "l":
                    translation = translation + "m"
                elif letter in "m":
                    translation = translation + "n"
                elif letter in "n":
                    translation = translation + "o"
                elif letter in "o":
                    translation = translation + "p"
                elif letter in "p":
                    translation = translation + "q"
                elif letter in "q":
                    translation = translation + "r"
                elif letter in "r":
                    translation = translation + "s"
                elif letter in "s":
                    translation = translation + "t"
                elif letter in "t":
                    translation = translation + "u"
                elif letter in "u":
                    translation = translation + "v"
                elif letter in "v":
                    translation = translation + "w"
                elif letter in "w":
                    translation = translation + "x"
                elif letter in "x":
                    translation = translation + "y"
                elif letter in "y":
                    translation = translation + "z"
                elif letter in "z":
                    translation = translation + "a"
                elif letter in "A":
                    translation = translation + "B"
                elif letter in "B":
                    translation = translation + "C"
                elif letter in "C":
                    translation = translation + "D"
                elif letter in "D":
                    translation = translation + "E"
                elif letter in "E":
                    translation = translation + "F"
                elif letter in "F":
                    translation = translation + "G"
                elif letter in "G":
                    translation = translation + "H"
                elif letter in "H":
                    translation = translation + "I"
                elif letter in "I":
                    translation = translation + "J"
                elif letter in "J":
                    translation = translation + "K"
                elif letter in "K":
                    translation = translation + "L"
                elif letter in "L":
                    translation = translation + "M"
                elif letter in "M":
                    translation = translation + "N"
                elif letter in "N":
                    translation = translation + "O"
                elif letter in "O":
                    translation = translation + "P"
                elif letter in "P":
                    translation = translation + "Q"
                elif letter in "Q":
                    translation = translation + "R"
                elif letter in "R":
                    translation = translation + "S"
                elif letter in "S":
                    translation = translation + "T"
                elif letter in "T":
                    translation = translation + "U"
                elif letter in "U":
                    translation = translation + "V"
                elif letter in "V":
                    translation = translation + "W"
                elif letter in "W":
                    translation = translation + "X"
                elif letter in "X":
                    translation = translation + "Y"
                elif letter in "Y":
                    translation = translation + "Z"
                elif letter in "Z":
                    translation = translation + "A"
                else:
                    translation = translation + letter
            return translation

        if __name__ == '__main__':
            s = input("Enter a phrase: ")
            result = translate(s)
            print("")
            print("Translation: " + result)


    def shift2():
        def translate(s):
            translation = ""
            for letter in s:
                if letter in "a":
                    translation = translation + "c"
                elif letter in "b":
                    translation = translation + "d"
                elif letter in "c":
                    translation = translation + "e"
                elif letter in "d":
                    translation = translation + "f"
                elif letter in "e":
                    translation = translation + "g"
                elif letter in "f":
                    translation = translation + "h"
                elif letter in "g":
                    translation = translation + "i"
                elif letter in "h":
                    translation = translation + "j"
                elif letter in "i":
                    translation = translation + "k"
                elif letter in "j":
                    translation = translation + "l"
                elif letter in "k":
                    translation = translation + "m"
                elif letter in "l":
                    translation = translation + "n"
                elif letter in "m":
                    translation = translation + "o"
                elif letter in "n":
                    translation = translation + "p"
                elif letter in "o":
                    translation = translation + "q"
                elif letter in "p":
                    translation = translation + "r"
                elif letter in "q":
                    translation = translation + "s"
                elif letter in "r":
                    translation = translation + "t"
                elif letter in "s":
                    translation = translation + "u"
                elif letter in "t":
                    translation = translation + "v"
                elif letter in "u":
                    translation = translation + "w"
                elif letter in "v":
                    translation = translation + "x"
                elif letter in "w":
                    translation = translation + "y"
                elif letter in "x":
                    translation = translation + "z"
                elif letter in "y":
                    translation = translation + "a"
                elif letter in "z":
                    translation = translation + "b"
                elif letter in "A":
                    translation = translation + "C"
                elif letter in "B":
                    translation = translation + "D"
                elif letter in "C":
                    translation = translation + "E"
                elif letter in "D":
                    translation = translation + "F"
                elif letter in "E":
                    translation = translation + "G"
                elif letter in "F":
                    translation = translation + "H"
                elif letter in "G":
                    translation = translation + "I"
                elif letter in "H":
                    translation = translation + "J"
                elif letter in "I":
                    translation = translation + "K"
                elif letter in "J":
                    translation = translation + "L"
                elif letter in "K":
                    translation = translation + "M"
                elif letter in "L":
                    translation = translation + "N"
                elif letter in "M":
                    translation = translation + "O"
                elif letter in "N":
                    translation = translation + "P"
                elif letter in "O":
                    translation = translation + "Q"
                elif letter in "P":
                    translation = translation + "R"
                elif letter in "Q":
                    translation = translation + "S"
                elif letter in "R":
                    translation = translation + "T"
                elif letter in "S":
                    translation = translation + "U"
                elif letter in "T":
                    translation = translation + "V"
                elif letter in "U":
                    translation = translation + "W"
                elif letter in "V":
                    translation = translation + "X"
                elif letter in "W":
                    translation = translation + "Y"
                elif letter in "X":
                    translation = translation + "Z"
                elif letter in "Y":
                    translation = translation + "A"
                elif letter in "Z":
                    translation = translation + "B"
                else:
                    translation = translation + letter
            return translation

        if __name__ == '__main__':
            s = input("Enter a phrase: ")
            result = translate(s)
            print("")
            print("Translation: " + result)


    def shift3():
        def translate(s):
            translation = ""
            for letter in s:
                if letter in "a":
                    translation = translation + "d"
                elif letter in "b":
                    translation = translation + "e"
                elif letter in "c":
                    translation = translation + "f"
                elif letter in "d":
                    translation = translation + "g"
                elif letter in "e":
                    translation = translation + "h"
                elif letter in "f":
                    translation = translation + "i"
                elif letter in "g":
                    translation = translation + "j"
                elif letter in "h":
                    translation = translation + "k"
                elif letter in "i":
                    translation = translation + "l"
                elif letter in "j":
                    translation = translation + "m"
                elif letter in "k":
                    translation = translation + "n"
                elif letter in "l":
                    translation = translation + "o"
                elif letter in "m":
                    translation = translation + "p"
                elif letter in "n":
                    translation = translation + "q"
                elif letter in "o":
                    translation = translation + "r"
                elif letter in "p":
                    translation = translation + "s"
                elif letter in "q":
                    translation = translation + "t"
                elif letter in "r":
                    translation = translation + "u"
                elif letter in "s":
                    translation = translation + "v"
                elif letter in "t":
                    translation = translation + "w"
                elif letter in "u":
                    translation = translation + "x"
                elif letter in "v":
                    translation = translation + "y"
                elif letter in "w":
                    translation = translation + "z"
                elif letter in "x":
                    translation = translation + "a"
                elif letter in "y":
                    translation = translation + "b"
                elif letter in "z":
                    translation = translation + "c"
                elif letter in "A":
                    translation = translation + "D"
                elif letter in "B":
                    translation = translation + "E"
                elif letter in "C":
                    translation = translation + "F"
                elif letter in "D":
                    translation = translation + "G"
                elif letter in "E":
                    translation = translation + "H"
                elif letter in "F":
                    translation = translation + "I"
                elif letter in "G":
                    translation = translation + "J"
                elif letter in "H":
                    translation = translation + "K"
                elif letter in "I":
                    translation = translation + "L"
                elif letter in "J":
                    translation = translation + "M"
                elif letter in "K":
                    translation = translation + "N"
                elif letter in "L":
                    translation = translation + "O"
                elif letter in "M":
                    translation = translation + "P"
                elif letter in "N":
                    translation = translation + "Q"
                elif letter in "O":
                    translation = translation + "R"
                elif letter in "P":
                    translation = translation + "S"
                elif letter in "Q":
                    translation = translation + "T"
                elif letter in "R":
                    translation = translation + "U"
                elif letter in "S":
                    translation = translation + "V"
                elif letter in "T":
                    translation = translation + "W"
                elif letter in "U":
                    translation = translation + "X"
                elif letter in "V":
                    translation = translation + "Y"
                elif letter in "W":
                    translation = translation + "Z"
                elif letter in "X":
                    translation = translation + "A"
                elif letter in "Y":
                    translation = translation + "B"
                elif letter in "Z":
                    translation = translation + "C"
                else:
                    translation = translation + letter
            return translation

        if __name__ == '__main__':
            s = input("Enter a phrase: ")
            result = translate(s)
            print("")
            print("Translation: " + result)



    def shift14():
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
            print("Translation: " + result)
    print("")
    shift = input("How many times would you like to shift the cypher? (1-26): ")
    print("")
    if shift == "1":
        shift1()
    elif shift == "2":
        shift2()
    elif shift == "3":
        shift3()
    elif shift == "4":
        shift4()
    elif shift == "5":
        shift5()
    elif shift == "6":
        shift6()
    elif shift == "7":
        shift7()
    elif shift == "8":
        shift8()
    elif shift == "9":
        shift9()
    elif shift == "10":
        shift10()
    elif shift == "11":
        shift11()
    elif shift == "12":
        shift12()
    elif shift == "13":
        shift13()
    elif shift == "14":
        shift14()
    elif shift == "15":
        shift15()
    elif shift == "16":
        shift16()
    elif shift == "17":
        shift17()
    elif shift == "18":
        shift18()
    elif shift == "19":
        shift19()
    elif shift == "20":
        shift20()
    elif shift == "21":
        shift21()
    elif shift == "22":
        shift22()
    elif shift == "23":
        shift23()
    elif shift == "24":
        shift24()
    elif shift == "25":
        shift25()
    elif shift == "26":
        shift26()
    else:
        print("Error: Invalid Input")
        print("Default Procedure: Exit to Menu")
        cypher1 = 1

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
