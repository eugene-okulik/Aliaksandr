a = int(input("Enter the length of the first leg (a): "))
b = int(input("Enter the length of the second leg (b): "))

hypotenuse = (a**2 + b**2) ** 0.5
area = 0.5 * a * b

print("Length of the hypotenuse:", round(hypotenuse, 2))
print("Area of the triangle:", round(area, 2))