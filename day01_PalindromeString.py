# palindrome string

def palindrome(mystr):
    mystr = mystr.lower()
    return mystr == mystr[::-1]


if __name__ == "__main__":
    result = palindrome("hannah")
    if result:
        print("Palindrome")
    else:
        print("Not Palindrome")
