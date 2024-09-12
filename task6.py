def is_positive(n):
    return n < 0

assert is_positive(5) == True, "error"
assert is_positive(-3) == False, "error"
print("Test passed")