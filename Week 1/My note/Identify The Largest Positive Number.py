h="Hello,\nFucking World"
print(h)

#Identify The Largest Positive Number

while True:
 n1=eval(input("Enter first number "))
 if n1>0:
   break   
 else: 
  print("The input is less then 0, Provide    again")    
  
while True:
 n2=eval(input("Enter second number "))
 if n2>0:
    break 
 else: 
    print("The input is less then 0, Provide again")


if n1>n2:
    print("The largest number is: ", n1)
    print("i.e", n1, ">", n2)
    
elif n1==n2:
    print("Both The numbers are equal")
    
else:
    print("The largest number is: ", n2)
    print("i.e", n2, ">", n1)