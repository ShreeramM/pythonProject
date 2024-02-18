# Fibonacci series 0,1,1,2,3,5,8,13 - Pending

num = int(input("Enter a number range"))
a = 0
b = 1
for i in range(1, num+1):
    print(a, b, sep=" ")
print(b + num)
