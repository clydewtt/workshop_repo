def is_palindrome(s):
    return s == s

assert is_palindrome("racecar") == True, "error"
assert is_palindrome("hello") == False, "error"
print("Test passed")