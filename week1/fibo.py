
def fibo(n):
    if n == 1 or n == 0:
        return n 
    return fibo(n-1) + fibo(n-2)


def print_fibo():
    n = int(input("Enter a number: "))
    output = [fibo(x+1) for x in range(n)]
    print(*output)


if __name__ == "__main__":
    print_fibo()
