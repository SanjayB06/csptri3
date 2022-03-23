class palindrome():
    def __init__(self,string):
        self.string = string
    def __call__(self):
        testStr = self.string.lower()
        for x in [" ",",","-","."]:
          testStr = testStr.replace(x,"")
        if testStr == testStr[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    pal = palindrome("race car")
    print(pal())    
    pal2 = palindrome("not a palindrome")
    print(pal2())
    pal3 = palindrome("A man, a plan, a canal -- Panama")
    print(pal3())