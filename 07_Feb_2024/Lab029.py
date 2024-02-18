# ternary operator
x = 10
y = 20
a = True
print(not a)  # False - ! is not allowed in python
if x > y:
    print(x)
else:
    print(y)

str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)
name = "Pramod"
age = 65
# print(name + age)  # TypeError: can only concatenate str (not "int") to str
print(name + str(age))  # Typecasting of name + age

g = "Hello"
g += "World"  # g= g+ "World"
print(g)

# Increement & Decreement Operator
x = 5
x += 1  # x = x+1
print(x)  # 6
x -= 1  # x = x-1
print(x)  # 5
