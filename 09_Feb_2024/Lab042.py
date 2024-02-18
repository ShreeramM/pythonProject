# Write a program that calculates grade score between 90 and 100 - a,80 to 89- b
# 70 to 79 - c.60 to 69 - d less 0 to 59 - e grade

score = int(input("Enter the score: "))

if score >= 90 and score <= 100:
    print("A grade")
elif score >= 80 and score <= 89:
    print("B grade")
elif score >= 70 and score <= 79:
    print("C grade")
elif score >= 60 and score <= 69:
    print("D grade")
elif score >= 50 and score <= 59:
    print("E grade")
else:
    print("Invalid input")