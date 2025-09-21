h="Hello, \nFucking World"
print(h)

n1=eval(input("Enter first number "))
n2=eval(input("Enter second number "))

if n1>n2:
    print("The largest number is: ", n1)
    print("i.e", n1, ">", n2)
    
elif n1==n2:
    print("Both numbers are equal: ", n1, "=", n2)
else:
    print("The largest number is: ", n2)
    print("i.e", n2, ">", n1)