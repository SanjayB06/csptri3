
class Palindrome:
    def __init__(self, string):
        self.string = string

    def __call__(self):
        test_str = self.string.lower()
        for x in [" ", ",", "-", "."]:
            test_str = test_str.replace(x, "")
        if test_str == test_str[::-1]:
            return True
        else:
            return False


def print_pal():
    string = input("Enter a word/sentence to test: ")
    pal = Palindrome(string)
    if pal():
        print("That is a palindrome! ")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    pal = Palindrome("race car")
    print(pal())    
    pal2 = Palindrome("not a palindrome")
    print(pal2())
    pal3 = Palindrome("A man, a plan, a canal -- Panama")
    print(pal3())
