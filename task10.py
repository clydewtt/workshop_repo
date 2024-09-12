def celsius_to_fahrenheit(c):
    return (c * 2) + 32

assert celsius_to_fahrenheit(0) == 32, "error"
assert celsius_to_fahrenheit(100) == 212, "error"
print("Test passed")