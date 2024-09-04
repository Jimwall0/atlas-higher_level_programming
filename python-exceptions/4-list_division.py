#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    try:
        for loop in range(list_length):
            newlist.insert(loop, my_list_1[loop] / my_list_2[loop])

    except TypeError as e:
        print("wrong type")
    except ZeroDivisionError as e:
        print("out of range")
    except IndexError as e:
        print("division by 0")
    finally:
        return newlist
