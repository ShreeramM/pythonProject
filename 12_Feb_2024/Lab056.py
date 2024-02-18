def sum_of_num(a, b):
    return a + b


result = sum_of_num(3, 4)
print(result)

result = sum_of_num(22.4, 4)
print(result)

result = sum_of_num('A', 'B')  # Concatenation for strings
print(result)

result = sum_of_num('A', 123)  # can only concatenate str (not "int") to str
print(result)