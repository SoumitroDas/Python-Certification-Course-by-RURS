'''Types of Function in Python (Built In, User define(Normal, return, lambda), Recursive  Function)
Keyword Def
Syntex 
def function_name(parameters):
    function body
    Statement
    return value
'''
h="Hello, \nFucking World"
print(h)
#Add three numbers using user define function

def ad(a, b, c):
    return a + b + c

def ad2(a, b, c):
    print("Sum of numbers using normal function is:", a + b + c )


a=eval(input("Enter first number: "))
b=eval(input("Enter second number: "))
c=eval(input("Enter third number: "))
print("Sum of numbers by using return function is: ", ad(a, b, c))

ad2(a, b, c)

print(pow(a,b))