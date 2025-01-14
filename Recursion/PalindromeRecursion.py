def check_palindrome(str,l=0):
    if l>= len(str)//2:
        return True
    
    if str[l] != str[len(str)-1-l]:
        return False

    return check_palindrome(str,l+1)

print(check_palindrome("MADAM"))