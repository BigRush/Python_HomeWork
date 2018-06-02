#!/usr/bin/env python3.6

def List_Sum (list):
    for i in list:
        j += int(i)
    return j

def User_Input (j):
    list = []
    j = 0
    while j <= 30:
        #try:
        user_num=int(input("Please enter a number: "))
        if user_num < 10:
            list += user_num
            j = List_Sum(list)
        else:
            break

    #    except:
    #        print("Invalid number plese try again")


User_Input (j)
