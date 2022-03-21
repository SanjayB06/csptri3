class factorial():
    def __init__(self,n):
        self.n = n
    def factorial(self):
        product = 1
        for x in range(1,self.n+1):
            product*=x
            print(product)
if __name__ == "__main__":
    fac = factorial(5)
    fac.factorial()