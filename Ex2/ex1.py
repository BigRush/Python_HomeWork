#!/usr/bin/env python3.6

def Input_A_Num ():
    try:
        a_num=int(input("Please enter a number: "))
        return a_num
    except:
        print("Invalid number plese try again")
        Input_A_Num ()


def Input_B_Num ():
    try:
        b_num=int(input("Please enter another number: "))
        return b_num
    except:
        print("Invalid number plese try again")
        Input_B_Num ()


def Compare_Nums (a_num, b_num):
    if a_num > b_num:
        print("{} is bigger than {}".format(a_num, b_num))
    elif a_num < b_num:
        print("{} is bigger than {}".format(b_num, a_num))
    elif a_num == b_num:
        print("{} and {} are equals".format(a_num, b_num))


def Sum_Nums (a_num, b_num):
    print("The summary of the numbers are: ", a_num + b_num)


def Divide_Nums (a_num, b_num):
    print("The devision of the numbers are: ", a_num / b_num)


def Multiply_Nums (a_num, b_num):
    print("The multiplication of the numbers are: ", a_num * b_num)


a_num = Input_A_Num ()
b_num = Input_B_Num ()

Compare_Nums (a_num, b_num)

Sum_Nums (a_num, b_num)

Divide_Nums (a_num, b_num)

Multiply_Nums (a_num, b_num)
