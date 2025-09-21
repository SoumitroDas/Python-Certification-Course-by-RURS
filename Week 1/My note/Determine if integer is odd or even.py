h="Hello, \nFucking World"
print(h)

#Determine if integer is odd or even

while True:
    x = eval(input("Enter an integer: "))
    
    if isinstance(x, int):break

    else:
        print(type(x))
        print("Invalid input. Please enter a valid integer.")

if x % 2 == 0:
    print("The number is even") 
else:
    print("The number is odd")

