
string=input("enter string:")
def palindrome(string):
    if(string==string[::-1]):
        print("string palindrome")
    else:
        print("string not palindrome")
palindrome(string)

