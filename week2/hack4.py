class palindrome():
    def __init__(self,string):
        self.string = string
    def checkifpal(self):
        testStr = self.string.lower()
        testStr = testStr.replace(" ","")
        testStr = testStr.replace(",","")
        testStr = testStr.replace("-","")
        testStr = testStr.replace(".","")
        if testStr == testStr[::-1]:
            return True
        else:
            return False

if __name__ == "__main__":
    pal = palindrome("race car")
    print(pal.checkifpal())    
    pal2 = palindrome("not a palindrome")
    print(pal2.checkifpal())
    pal3 = palindrome("A man, a plan, a canal -- Panama")
    print(pal3.checkifpal())