from menulist import mainMenu
import os

def buildMenu(menu):
    for key, value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")  # each menu item is printed
    print("What is your choice? (enter the number value) ")  # user input promp

# def menuAnim():
#     for x in range(50):
#         if x!= 50:
#             print(" "*x," \\")
#             print(" "*x,"    === \\")
#             print(" "*x,"          |")
#             print(" "*x,"    === //")
#             print(" "*x," //")
#             os.system("clear")
#         else:
#             print(" "*x," \\")
#             print(" "*x,"    === \\")
#             print("Python Main Menu "*x,"          |")
#             print(" "*x,"    === //")
#             print(" "*x," //")

def presentMenu(menu):
    buildMenu(menu)  # print out menu and take input
    choice = (input())
    while choice.isalpha():
        choice = input("Please enter a number: ")
    choice = int(choice)
    while choice not in menu:  # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if choice in menu:
        if menu[choice]["type"] == "func":  # determine whether recursion is needed
            menu[choice]["exec"]()  # run function

        else:
            presentMenu(menu[choice]["exec"])  # display submenu


if __name__ == "__main__":
    while True:  # forever loop
        # menuAnim()
        presentMenu(mainMenu)
        halt = input("Do you want to continue (y/n)? ")  # checks if user wants to go again
        if halt.lower() == "n":
            break
