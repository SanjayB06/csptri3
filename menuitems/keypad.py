def print_matr(matr):
    for x in matr:
        print(*x)

if __name__ == "__main__":
    print_matr([[1,2,3],[4,5,6],[7,8,9],["*",0,"#"] ])