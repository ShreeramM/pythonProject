#table of 2

# num = int(input("Enter a number range: "))
#
# print(f"Table of num is {num}*1 = {num*1}")
# print(f"Table of num is {num}*2 = {num*2}")
# print(f"Table of num is {num}*3 = {num*3}")
# print(f"Table of num is {num}*4 = {num*4}")
# print(f"Table of num is {num}*5 = {num*5}")
# print(f"Table of num is {num}*6 = {num*6}")
# print(f"Table of num is {num}*7 = {num*7}")
# print(f"Table of num is {num}*8 = {num*8}")
# print(f"Table of num is {num}*9 = {num*9}")
# print(f"Table of num is {num}*10 = {num*10}")
# print('------')

num =0
num1 = int(input("Enter a starting range: "))
num2 = int(input("Enter a ending range: "))
for i in range(num1,num2):
 for j in range(1,10):
  print(f"Table of num is {num1}*{j} = {num1*j}")
 num1 = num1 + 1
 num2 = num2 + 1
print('------')
for j in range(1, 10):
  print("Table of num is ", num, '*', j,'=', num*j)