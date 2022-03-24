# Hack 3: create your own math function

# Function is superfactorial: superfactorial is product of all factorials until n. 

# OOP method
class superFactorial():
    def __init__(self,n):
        self.n = n
    def factorial(self,y):
        y = self.n if y is None else y
        product = 1
        for x in range(1,y+1):
            product*=x
        return product
    def __call__(self):
        product = 1
        for x in range(1,self.n+1):
            product*= self.factorial(x)
        return product

# Imperative Method
def superfac():
    x = int(input("What number should we use? "))
    product = 1
    for y in range(1,x+1):
        secondProd = 1
        for z in range(1,y+1):
            secondProd*= z
        product*=secondProd
    print(product)
if __name__ == "__main__":
    sfac = superFactorial(3)
    print(sfac())
    print(superfac())