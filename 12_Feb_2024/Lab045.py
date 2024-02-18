# break
# for i in range(1,10):
#     print(i)
# for i in range(1,11,1):
#     print(i)
for counter in range(1, 11):
    if counter == 5:
        break
    print(counter)
print("Outside of the loop")

for counter in range(0, 11): #0, 1, 2, 3, 4, 5
    print(counter)
    if counter == 5:
        break
print("Outside of the loop")