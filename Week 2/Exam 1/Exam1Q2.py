'''Question 02:
 Make a user defined function square() to calculate the square of a
number.'''
h="Hello, \nFucking World"
print(h)

def square(n):
    """Returns the square of the given number."""
    return n * n

x= eval(input("Enter a number to find its square: "))
print("The square of", x, "is", square(x))