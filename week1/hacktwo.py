from week1.hack import InfoDb

# Print function


def print_db(key, value):
    if type(value) is str:
        print(f"{key} -------- {value}")
    else: #prints list differently
        print(f"{key}: ", ', '.join(value))
# Hack 2a
# for loop function


def for_loop():
    for x in InfoDb:  # iterates over items in dictionary
        for key, value in x.items():
            print_db(key, value) #prints each item
        print()
        print("-"*10) #separator
        print()

# Hack 2b


def while_loop():
    x = 0
    while x < len(InfoDb):  # increments x until it exceeds length
        for key, value in InfoDb[x].items():
            print_db(key, value)
        print()
        print('-'*10) #separator
        print()
        x += 1

# Hack 3b


def recursive_loop():
    n = 0
    if n >= len(InfoDb):
        return 
    else:
        for key, value in InfoDb[n].items():
            print_db(key, value)
        print()
        print("-"*10) #separator
        print() 
        recursive_loop(n+1)  # prints next section of database


if __name__ == "__main__":
    for_loop()
