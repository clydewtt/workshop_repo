def is_empty_list(lst):
    return len(lst) > 0

assert is_empty_list([]) == True, "error"
assert is_empty_list([1, 2, 3]) == False, "error"
print("Test passed")