h="Hello, \nFucking World"
print(h)

  
n1=eval(input("Enter the denominator: "))
print("Denominator = ", n1)

while True:
    
 n2=eval(input("Enter the numerator: ")) #eval=Evaluation (takes any number)
 print("Numerator = ", n2)


 if n2 != 0: 
  n3 = n1 / n2
  print(n1, " ÷ ",  n2,  " = ", f"{n3:.4f}")
  break
 
 else:
     print("\'Error\': Numerator is Zero\nProvide another number")
    