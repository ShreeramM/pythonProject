# Find maximum of  numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print("Num1 is greater")
elif num2 > num3 and num2 > num1:
    print("Num2 is greater")
else:
    print("Num3 is greater")
