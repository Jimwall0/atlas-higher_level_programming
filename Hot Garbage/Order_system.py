#!/usr/bin/python3
def o_system():
    menu_item = {
        "Lasagna": 13,
        "Bolagna": 13.25,
        "Spam": 5,
        "Fruits": 8
    }
    total = 0
    order = ["Spam", "Lasagna", "Bolagna"]
    print(menu_item)
    for loop in range(len(order)):
        print("{} price: {}".format(order[loop], menu_item[order[loop]])) # This prints menu item with it's price
        total += menu_item[order[loop]]
    print(round(total + (total * 0.1), 2)) # This is your total
    return total

if __name__ == "__main__":
    o_system
    print("FUnny things")
