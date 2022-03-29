# import os
# was not being used
import time


def print_ship():
    print("Honestly anything less than 50 is like nothing ")
    print("And more than 100 is like past the screen")
    distance = int(input("So, how far should the ship go? "))
    for x in range(int(distance)):
        print("  "*x, "    |\ ")
        print("  "*x, "    |/ ")
        print("  "*x, "\__ |__/ ")
        print("  "*x, " \____/ ")
        print("\u001b[34m {dashes} \u001b[37m".format(dashes="--"*distance))

        # os.system("clear")
        time.sleep(0.006)


if __name__ == "__main__":
    print_ship()
