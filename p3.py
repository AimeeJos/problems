# Check palindrome number

def check_pallindrome(string):
    if str(string) == str(string)[::-1]:
        return "is a pallindrome"
    else:
        return "not a pallindrome"
    
print(check_pallindrome("madam"))
print(check_pallindrome(1210))