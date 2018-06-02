#!/usr/bin/env python3.6

def Input_A_Str ():
    try:
        a_str = str(input("Please enter a text: "))
        return a_str
    except:
        print("Invalid string plese try again")
        Input_A_Str ()


def Input_B_Str ():
    try:
        b_str = str(input("Please enter another text: "))
        return b_str
    except:
        print("Invalid string plese try again")
        Input_B_Str ()


def Input_Num ():
    try:
        a_num = int(input("Please enter a number between 1-3: "))
        if a_num >= 1 and a_num <= 3:
            return a_num
        else:
            print("Nuber is not between 1-3")
            Input_Num ()
    except:
        print("Invalid number plese try again")
        Input_Num ()


a_num = Input_Num ()
a_str = Input_A_Str ()
b_str = Input_B_Str ()

def Compare_Str (a_str, b_str):
    a_len = len(a_str)
    b_len = len(b_str)

    ## compare string lengths
    if a_len > b_len:
        print("{} is longer than {}".format(a_str, b_str))
        c_str = a_str[0:a_num]
        print("{} are the first {} characters of {}".format(c_str, a_num, a_str))
        temp_str = b_str[0:1]
        if temp_str in a_str:
            print(a_str.replace(temp_str, "BigRush"))

        merge_str = ""
        for i in (a_str, b_str, c_str):
            merge_str += str(i)
            
        j = 0
        for i in merge_str:
            if i == "A":
                j += 1
        print("A was in {} times in {}".format(j, merge_str))

    elif a_len < b_len:
        print("{} is longer than {}".format(b_str, a_str))
        c_str = b_str[0:a_num]
        print("{} are the first {} characters of {}".format(c_str, a_num, b_str))
        temp_str = a_str[0:1]
        if temp_str in b_str:
            print(b_str.replace(temp_str, "BigRush"))

        merge_str = ""
        for i in (a_str, b_str, c_str):
            merge_str += str(i)

        j = 0
        for i in merge_str:
            if i == "A":
                j += 1
        print("A was in {} times in {}".format(j, merge_str))

    elif a_len == b_len:
        print("{} and {} has equal length".format(a_str, b_str))

    ## if string is found in another string
    if a_str in b_str and b_str not in a_str:
        print("{} is in {}".format(a_str, b_str))

    elif b_str in a_str and a_str not in b_str:
        print("{} is in {}".format(b_str, a_str))

    elif a_str == b_str:
        print("{} is in {} and the other way around".format(a_str, b_str))

    else:
        print("{} isn't in {} and {} isn't in {}".format(a_str, b_str, b_str, a_str))

def fun(a_num):
    print(a_num)

fun (a_num)

Compare_Str (a_str, b_str)
