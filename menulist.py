from week0.christmastree import print_tree
from week0.ship import print_ship
from tri2.keypad import print_matr
from tri2.swap import swap
from week1.fibo import fibo, print_fibo
from week1.hack import InfoDb
from week1.hacktwo import for_loop, while_loop, recursive_loop
from week2.hack2 import dispfac
from week2.hack2 import disp_series
from week2.hack3 import superfac
from week2.hack4 import print_pal
# from Cross_Over import Affirmations


def f1():
    print('f1')


def f2():
    print('f2')


subMenu = {
    1: {"display": "f1",
        "exec": f1,
        "type": "func"},
    2: {"display": "f2",
        "type": "func",
        "exec": f2, },
    3: {
        "display": "Quit program",
        "exec": quit,
        "type": "func"
    }

}
week1hack2Menu = {
    1: {
        "display": "Hack 2a (for loop)",
        "exec": for_loop,
        "type": "func"
    },
    2: {
        "display": "Hack 2b (while loop)",
        "exec": while_loop,
        "type": "func"
    },
    3: {
        "display": "Hack 2c (recursive)",
        "exec": recursive_loop,
        "type": "func"
    },
    4: {
        "display": "Quit program",
        "exec": quit,
        "type": "func"
    },
}
drawingMenu = {
    1: {
        "display": "Christmas Tree",
        "exec": print_tree,
        "type": "func"
    },
    2: {
        "display": "Print Ship",
        "exec": print_ship,
        "type": "func"
    },
    3: {
        "display": "Keypad",
        "exec": print_matr,
        "type": "func"
    },
    4: {
        "display": "quit",
        "exec": quit,
        "type": "func"
    },
    # 5: {
    #     "display": "Affirmations",
    #     "exec": Affirmations,
    #     "type": "func"
    # }
}
factorialMenu = {
  1: {
    "display": "Factorial calculator",
    "exec": dispfac,
    "type": "func"
  },
  2: {
    "display": "Factorial series",
    "exec": disp_series,
    "type": "func"
  },
  3: {
    "display": "Superfactorial",
    "exec": superfac,
    "type": "func"
  },
  4: {
    "display": "Quit",
    "exec": quit,
    "type": "func"
  }
}
mathMenu = {
    1: {
        "display": "Fibonacci",
        "exec": print_fibo,
        "type": "func"
    },
    2: {
        "display": "Factorials",
        "exec": factorialMenu,
        "type": "submenu"
    },
    3: {
        "display": "quit",
        "exec": quit,
        "type": "func"
    }
}

mainMenu = {
    1: {
        "display": "Drawings",
        "exec": drawingMenu,
        "type": "submenu"
    },
    2: {"display": "Swap ",
        "exec": swap,
        "type": "func"},
    3: {
        "display": "Submenu",
        "exec": subMenu,
        "type": "submenu"
    },
    4: {
        "display": "Week 1 Hack 2 (InfoDb)",
        "exec": week1hack2Menu,
        "type": "submenu"
    },
    5: {
        "display": "Math Functions",
        "exec": mathMenu,
        "type": "submenu"
    },
    6: {
        "display": "Palindrome",
        "exec": print_pal,
        "type": "func"
    },
    7: {
        "display": "Quit program",
        "exec": quit,
        "type": "func"
    }
}
