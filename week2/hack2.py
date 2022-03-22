class factorial():
    def __init__(self,n):
        self.n = n
    def factorial(self,y=None):
        y = self.n if y is None else y
        product = 1
        for x in range(1,y+1):
            product*=x
        return product
    def __call__(self):
      series = [str(self.factorial(x)) for x in range(1,self.n+1)]
      return ( " ".join(series))
def dispfac():
  n = int(input("What factorial do you want? "))
  fac = factorial(n)
  print(fac.factorial())
def dispSeries():
  n = int(input("How long should the series be? "))
  fac = factorial(n)
  print(fac())
if __name__ == "__main__":
    fac = factorial(6)
    print(fac.factorial())
    print(fac())