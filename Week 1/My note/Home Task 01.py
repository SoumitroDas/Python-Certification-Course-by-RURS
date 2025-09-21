h="Hello, \nFucking World"
print(h)


while True:
 num1 = eval(input("Enter first number: "))
 num2 = eval(input("Enter second number: "))

 if num1 > 0 and num2 > 0:
 
    if num1 > num2:
        print("The larger number is:", num1)
        break
    elif num2 > num1:
        print("The larger number is:", num2)
        break
    else:
        print("Both numbers are equal.")
        break
 else:
    print("Invalid! Please enter numbers greater than 0.")
