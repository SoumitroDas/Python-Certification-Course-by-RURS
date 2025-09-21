h="Hello, \nFucking World"
print(h)
#Calculating the area of a triangle using a function

import math 

# Method 1: Base and Height
def Abh(b, h):
    return b*h/2

# Method 2: Three sides (Heron's Formula)
def Ah(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Method 3: Two sides and included angle
def AabTheta(a, b, theta):
    angle_rad = math.radians(theta)  # convert degrees to radians
    return 0.5 * a * b * math.sin(angle_rad)

print("Triangle Area Calculation Methods:")
print("1. Using Base and Height")
print("2. Using Three Sides (Heron's Formula)")
print("3. Using Two Sides and Included Angle")

ch = int(input("Enter your choice (1/2/3): "))

if ch == 1:
    b = eval(input("Enter base: "))
    h = eval(input("Enter height: "))
    print("Area =", Abh(b, h))

elif ch == 2:
    a = eval(input("Enter side a: "))
    b = eval(input("Enter side b: "))
    c = eval(input("Enter side c: "))
    print("Area =", Ah(a, b, c))

elif ch == 3:
    a = eval(input("Enter side a: "))
    b = eval(input("Enter side b: "))
    t = eval(input("Enter included angle (in degrees): "))
    print("Area =", AabTheta(a, b, t))

else:
    print("Invalid choice!")

