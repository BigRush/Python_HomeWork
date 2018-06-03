#!/usr/bin/env python3.6

list = []
def User_Input (list):
    try:
        j = 0
        user_num = int(input("Please anter a number: "))
        list.append(user_num)
        print("List now: {}".format(list))
        for i in list:
            print ("i now: {}".format(i))
            j += int(i)
            if j > 30:
                print("Summary: {}".format(j))
                break
        while user_num < 10:
            try:
                j = 0
                user_num = int(input("Please anter a number: "))
                list.append(user_num)
                print("List now: {}".format(list))
                for i in list:
                    print ("i now: {}".format(i))
                    j += int(i)
                    if j > 30:
                        print("Summary: {}".format(j))
                        break
            except:
                print("Invalid number plese try again")
                User_Input (list)

        while user_num < 10 or j < 30:
            User_Input (list)

        print(j)
        exit()
    except:
        print("Invalid number plese try again")
        User_Input (list)

#user_num = User_Input ()







User_Input(list)
