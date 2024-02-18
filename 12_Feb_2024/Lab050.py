# Factorial of a number i.e 5 is 120

number = int(input("Enter a number: "))
# fact = 1
# for i in range(1, number + 1):
#     fact = fact * i
# print(fact)
    
#Own Logic
for i in range(1,number):
    number = number * i
print(number)