#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for loop in range(list_length):
        try:
            newlist.append(my_list_1[loop] / my_list_2[loop])

        except ZeroDivisionError:
            print("out of range")
            newlist.append(0)

        except TypeError:
            print("wrong type")
            newlist.append(0)

        except IndexError:
            print("division by 0")
            newlist.append(0)
        
        finally:
            continue
    return (newlist)