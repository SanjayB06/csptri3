# Spams Compliments
def speak():
    b = 0
    while compliment == 1:
        print(user + " is great")
        b = b + 1
        if b >= 250000:
            options()
            ask()
            break
    while compliment == 2:
        print(user + " is sooo smart")
        b = b + 1
        if b >= 250000:
            options()
            ask()
            break
    while compliment == 3:
        print(user + " is such a hard worker")
        b = b + 1
        if b >= 250000:
            options()
            ask()
            break
    while compliment == 727:
        print(user + " no one codes like " + user)
        print()
        print()
        print()
        print(user + " no thinks like  " + user)
        print()
        print()
        print()
        print(user + " no one's deployment plan is as great as  " + user)
        print()
        print()
        print()
        b = b + 1
        if b >= 50000:
            options()
            ask()
            break


# saved items
Options = ["1 - great", "2 - smart", "3 - hard-worker", "727 - ?????"]
Border = "----------------"
compliment = "un-picked"


# presents compliment options
def options():
    print()
    print(Border)
    for x in Options:
        print(x)
    print(Border)
    print()


options()

# Making it personal
user = input("Hiya what's your name: ")


# made it a function so I can re-ask
def ask():
    print()
    global compliment
    compliment = int(input("now which option do you want?: "))
    if compliment != 1 or 2 or 3 or 727:
        print("Please pick a proper option")
    speak()


# asking which one they want
ask()
