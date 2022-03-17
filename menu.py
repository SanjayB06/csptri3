from week0.christmastree import printTree
from week0.ship import printShip
from tri2.keypad import print_matr
from tri2.swap import swap
from week1.fibo import fibo,printFibo
from week1.hack import InfoDb
from week1.hacktwo import for_loop,while_loop,recursive_loop
def f1():
    print('f1')
def f2():
    print('f2')

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    while choice not in menu:
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()

        else:
            presentMenu(menu[choice]["exec"])
subMenu = {
    1: {"display":"f1",
    "exec":f1,
    "type":"func"},
    2: {"display":"f2",
    "type":"func",
    "exec":f2,},
    3: {
        "display": "Quit program",
        "exec":quit,
        "type":"func"
    }

}
hack2Menu = {
    1: {
        "display":"Hack 2a",
        "exec": for_loop,
        "type":"func"
    },
    2: {
        "display":"Hack 2a",
        "exec": recursive_loop,
        "type":"func"
    },
    1: {
        "display":"Hack 2a",
        "exec": while_loop,
        "type":"func"
    },
    4: {
        "display":"Quit program",
        "exec": quit,
        "type":"func"
    },
}
mainMenu = {
    1: {"display":"Christmas Tree",
    "exec":printTree,
    "type":"func"},
    2: {"display":"Ship",
    "exec":printShip,
    "type":"func"},
    3: {"display":"Keypad ",
    "exec":print_matr,
    "type":"func"},
    4: {"display":"Swap ",
    "exec":swap,
    "type":"func"},
    5: {
        "display":"Submenu",
        "exec": subMenu,
        "type":"submenu"
    },
    6: {
        "display":"Fibonacci",
        "exec": printFibo,
        "type":"func"
    },
    7: {
        "display":"Hack 2",
        "exec": hack2Menu,
        "type":"submenu"
    },
    8: {
        "display": "Quit program",
        "exec":quit,
        "type":"func"
    }
}

if __name__ == "__main__":
    while True:
        presentMenu(mainMenu)
        halt = input("Do you want to continue (y/n)? ")
        if halt.lower() == "n":
            break