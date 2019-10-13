def is_palindrome(input):
    if len(input) < 2:
        return True
    if input[0] == input[-1]:
        return is_palindrome(input[1:-1])
    else:
        return False

print(is_palindrome("tacocat"))
print(is_palindrome("amanaplanacanalpanama"))
print(is_palindrome("andy"))