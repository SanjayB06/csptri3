def printTree():
    row = int((input("How large should the tree be? ")))
    for x in range(row):
        x+=1
        spaces = row-x
        print(" "*spaces,"* "*x)
    print(" "*(row-3),"* "*3)
    print(" "*(row-3),"* "*3)
if __name__ == "__main__":
    printTree()