
from math import *
import math
from logging.config import RESET_ERROR
from math import *
import random
import turtle
import time
from random import *
import datetime
import winsound
from threading import *
from tkinter import *
from tkinter.simpledialog import askinteger
from tkinter import messagebox
from turtledemo.sorting_animate import show_text
import threading, keyword
num1 = 0
num2 = 0
op = 0
ans = 0
num = 0
neg = 1
prevans = 0
stilneg = 1
dec = 0
dec1 = 10
top = Tk()
top.geometry("500x500")
text = Text(top)
top.title("Calculator")
text.pack()


print("This display is for debugging.")
print("num1 =", num1)
print("num2 =", num2)
print("op =", op)
print("ans =", ans)
print("num =", num)
print("neg =", neg)
print("prevans =", prevans)
print("stilneg =", stilneg)
print("dec =", dec)
print("dec1 =", dec1)


def one():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 1
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA/dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA/dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def two():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 2
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def three():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 3
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def four():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 4
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def five():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 5
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)

def six():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 6
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def seven():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 7
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def eight():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 8
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def nine():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 9
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def zero():
    global num
    global neg
    global stilneg
    global dec
    global dec1
    numA = 0
    if neg == 1 and dec == 0:
        num = ((num * 10) + numA)
    elif neg == -1 and dec == 0:
        num = ((num * 10) - numA)
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    elif neg == 1 and dec == 1:
        num = num + (numA / dec1)
        dec1 *= 10
    elif neg == -1 and dec == 1:
        num = num - (numA / dec1)
        dec1 *= 10
        if stilneg == -1:
            num = num * -1
            stilneg = 1
        else:
            stilneg = 1
    print(num)


def sign():
    global neg
    global stilneg
    if neg == 1:
        neg = -1
        stilneg = 1
    elif neg == -1:
        neg = 1
        stilneg = -1
    if neg == 1:
        print("pos")
    elif neg == -1:
        print("neg")
    else:
        print("Note to creator: You have somehow made it so that the sign is neither + or -. Please fix it.")



def plus():
    global op
    global num
    global num1
    global num2
    global sign
    global neg
    global stilneg
    global dec
    global dec1
    global ans1
    if op == 0:
        num1 = num
    if op == "+":
        num1 = (num1 + num)
    elif op == "-":
        num1 = (num1 - num)
    elif op == "*":
        num1 = (num1 * num)
    elif op == "/":
        if num == 0 and op == "/":
            num1 = ("Undefined")
        else:
            num1 = (num1 / num)
    elif op == "^":
        num1 = (num1 ** num)
    elif op == "√":
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num, num1)
        else:
            ans = math.log(num, num1)
    num = num2
    op = "+"
    print(op)
    dec = 0
    dec1 = 10
    neg = 1
    stilneg = 1



def minus():
    global op
    global num
    global num1
    global num2
    global neg
    global stilneg
    global dec
    global dec1
    if op == 0:
        num1 = num
    if op == "+":
        num1 = (num1 + num)
    elif op == "-":
        num1 = (num1 - num)
    elif op == "*":
        num1 = (num1 * num)
    elif op == "/":
        if num == 0 and op == "/":
            num1 = ("Undefined")
        else:
            num1 = (num1 / num)
    elif op == "^":
        num1 = (num1 ** num)
    elif op == "√":
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num, num1)
        else:
            ans = math.log(num, num1)
    num = num2
    op = "-"
    print(op)
    dec = 0
    dec1 = 10
    neg = 1
    stilneg = 1


def times():
    global op
    global num
    global num1
    global num2
    global neg
    global stilneg
    global dec
    global dec1
    if op == 0:
        num1 = num
    if op == "+":
        num1 = (num1 + num)
    elif op == "-":
        num1 = (num1 - num)
    elif op == "*":
        num1 = (num1 * num)
    elif op == "/":
        if num == 0 and op == "/":
            num1 = ("Undefined")
        else:
            num1 = (num1 / num)
    elif op == "^":
        num1 = (num1 ** num)
    elif op == "√":
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num, num1)
        else:
            ans = math.log(num, num1)
    num = num2
    op = "*"
    print(op)
    dec = 0
    dec1 = 10
    neg = 1
    stilneg = 1

def divide():
    global op
    global num
    global num1
    global num2
    global neg
    global stilneg
    global dec
    global dec1
    if op == 0:
        num1 = num
    if op == "+":
        num1 = (num1 + num)
    elif op == "-":
        num1 = (num1 - num)
    elif op == "*":
        num1 = (num1 * num)
    elif op == "/":
        if num == 0 and op == "/":
            num1 = ("Undefined")
        else:
            num1 = (num1 / num)
    elif op == "^":
        num1 = (num1 ** num)
    elif op == "√":
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num, num1)
        else:
            ans = math.log(num, num1)
    num = num2
    op = "/"
    print(op)
    dec = 0
    dec1 = 10
    neg = 1
    stilneg = 1


def square():
    global op
    global num
    global num1
    global num2
    global neg
    global stilneg
    global dec
    global dec1
    if op == 0:
        num1 = num
    if op == "+":
        num1 = (num1 + num)
    elif op == "-":
        num1 = (num1 - num)
    elif op == "*":
        num1 = (num1 * num)
    elif op == "/":
        if num == 0 and op == "/":
            num1 = ("Undefined")
        else:
            num1 = (num1 / num)
    elif op == "^":
        num1 = (num1 ** num)
    elif op == "√":
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num, num1)
        else:
            ans = math.log(num, num1)
    num = num2
    op = "^"
    print(op)
    dec = 0
    dec1 = 10
    neg = 1
    stilneg = 1

def root():
    global op
    global num
    global num1
    global neg
    global stilneg
    global dec
    global dec1
    if op == 0:
        num1 = num
    if op == "+":
        num1 = (num1 + num)
    elif op == "-":
        num1 = (num1 - num)
    elif op == "*":
        num1 = (num1 * num)
    elif op == "/":
        if num == 0 and op == "/":
            num1 = ("Undefined")
        else:
            num1 = (num1 / num)
    elif op == "^":
        num1 = (num1 ** num)
    elif op == "√":
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2 * -1) ** (1 / num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1 / num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2 * -1) ** (1 / num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1 / num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num, num1)
        else:
            ans = math.log(num, num1)
    num = num2
    dec = 0
    dec1 = 10
    neg = 1
    stilneg = 1
    op = "√"
    print(op)

def log():
    global op
    global num
    global num1
    global neg
    global stilneg
    global dec
    global dec1
    if op == 0:
        num1 = num
    if op == "+":
        num1 = (num1 + num)
    elif op == "-":
        num1 = (num1 - num)
    elif op == "*":
        num1 = (num1 * num)
    elif op == "/":
        if num == 0 and op == "/":
            num1 = ("Undefined")
        else:
            num1 = (num1 / num)
    elif op == "^":
        num1 = (num1 ** num)
    elif op == "√":
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2 * -1) ** (1 / num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1 / num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2 * -1) ** (1 / num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1 / num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num, num1)
        else:
            ans = math.log(num, num1)
    num = num2
    dec = 0
    dec1 = 10
    neg = 1
    stilneg = 1
    op = "log"
    print(op)

def decimal():
    global dec
    dec = 1
    print("dec")

def clear():
    print("Reset all numbers to 0")
    print("Operater set to +")
    print("Set sign to 0")
    global num1
    num1 = 0
    global num2
    num2 = 0
    global num
    num = 0
    global op
    op = 0
    global prevans
    prevans = 0
    global neg
    neg = 1
    global stilneg
    stilneg = 1
    global dec
    dec = 0
    global dec1
    dec1 = 10

def exit1():
    exit()

def ans():
    global num
    num = prevans
    print(num)

def pi():
    global num
    if neg == 1:
        num = math.pi
    elif neg == -1:
        num = math.pi * -1
    else:
        print("PI ERROR")
    print(num)

def e():
    global num
    if neg == 1:
        num = math.e
    elif neg == -1:
        num = math.e * -1
    else:
        print("E ERROR")
    print(num)

def equal():
    print("=")
    global prevans
    global ans
    global num1
    global num2
    global op
    global num
    global dec
    global dec
    global dec1
    if op == 0:
        op = "+"
    num2 = num
    if op == "+":
        ans = (num1 + num2)
    elif op == "-":
        ans = (num1 - num2)
    elif op == "*":
        ans = (num1 * num2)
    elif op == "/":
        if num2 == 0 and op == "/":
            ans = ("Undefined")
        else:
            ans = (num1 / num2)
    elif op == "^":
        ans = (num1 ** num2)
    elif op == "√":
        #copy paste this section below into all the operators
        if num1 == 0:
            num1 = 2
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
        else:
            if num2 < 0 and num2 != -1:
                ans = str((num2*-1) ** (1/num1)) + "i"
            elif num2 == -1 and num1 == 2:
                ans = "i"
            else:
                ans = num2 ** (1/num1)
    elif op == "log":
        if num2 == 0:
            ans = "Undefined"
        elif num2 < 0:
            ans = "Undefined"
        elif num1 == 0:
            num1 = 10
            ans = math.log(num2, num1)
        else:
            ans = math.log(num2, num1)
    global text
    if op != "log":
        top.update()
        text.insert(INSERT, num1)
        text.insert(INSERT, " ")
        text.insert(INSERT, op)
        text.insert(INSERT, " ")
        text.insert(INSERT, num2)
        text.insert(INSERT, " ")
        text.insert(INSERT, "=")
        text.insert(INSERT, " ")
        text.insert(INSERT, ans)
        text.insert(INSERT, "      ")
    elif op == "log":
        top.update()
        text.insert(INSERT, op)
        text.insert(INSERT, " ")
        text.insert(INSERT, num1)
        text.insert(INSERT, " (")
        text.insert(INSERT, num2)
        text.insert(INSERT, ") ")
        text.insert(INSERT, "=")
        text.insert(INSERT, " ")
        text.insert(INSERT, ans)
        text.insert(INSERT, "      ")
    text.pack()
    print(num1, op, num2, "=", ans)
    prevans = ans
    num1 = 0
    num2 = 0
    num = 0
    op = 0
    dec = 0
    dec1 = 10
    global neg
    neg = 1
    global stilneg
    stilneg = 1
    print("Reset both numbers to 0")
    print("Operater set to +")
    print("Set ANS to ", prevans)
    print("Set sign to 0")

button1 = Button(top, text="1", command=one)
button1.place(x=50, y=50)

button2 = Button(top, text="2", command=two)
button2.place(x=100, y=50)

button3 = Button(top, text="3", command=three)
button3.place(x=150, y=50)

button4 = Button(top, text="4", command=four)
button4.place(x=50, y=100)

button5 = Button(top, text="5", command=five)
button5.place(x=100, y=100)

button6 = Button(top, text="6", command=six)
button6.place(x=150, y=100)

button7 = Button(top, text="7", command=seven)
button7.place(x=50, y=150)

button8 = Button(top, text="8", command=eight)
button8.place(x=100, y=150)

button9 = Button(top, text="9", command=nine)
button9.place(x=150, y=150)

button0 = Button(top, text="0", command=zero)
button0.place(x=100, y=200)

buttonP = Button(top, text="+", command=plus)
buttonP.place(x=300, y=50)

buttonM = Button(top, text="-", command=minus)
buttonM.place(x=340, y=50)

buttonT = Button(top, text="*", command=times)
buttonT.place(x=375, y=50)

buttonD = Button(top, text="/", command=divide)
buttonD.place(x=410, y=50)

buttonS = Button(top, text="^", command=square)
buttonS.place(x=300, y=100)

buttonR = Button(top, text="√", command=root)
buttonR.place(x=350, y=100)

buttonE = Button(top, text="=", command=equal)
buttonE.place(x=350, y=200)

buttonC = Button(top, text="Reset Numbers", command=clear)
buttonC.place(x=225, y=400)

buttonSI1 = Button(top, text="+-", command=sign)
buttonSI1.place(x=350, y=150)

buttonE1 = Button(top, text="EXIT", command=exit1)
buttonE1.place(x=400, y=400)

buttonAns = Button(top, text="ANS", command=ans)
buttonAns.place(x=400, y=150)

buttonDec = Button(top, text=".", command=decimal)
buttonDec.place(x=300, y=150)

buttonLog = Button(top, text="log", command=log)
buttonLog.place(x=400, y=100)

buttonPi = Button(top, text="π", command=pi)
buttonPi.place(x=50, y=200)

buttonE2 = Button(top, text="e", command=e)
buttonE2.place(x=150, y=200)


top.mainloop()
