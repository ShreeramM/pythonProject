# Triangle Classifier
side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side2 == side3 or side1 == side2 or side1 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")