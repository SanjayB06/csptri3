from tkinter import N


def fibo(n):
    if n == 1 or n==0:
        return n 
    try:
        return fibo(n-1) + fibo(n-2)
    except RecursionError:
        return 0
    finally:
        return "Sorry, there was an error with your input"

def printFibo(n):
    output = [fibo(x+1) for x in range(n)]
    return output
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(*printFibo(num))