h="Hello, \nF*cking World"
print(h)

#Grading System Program

print("Welcome to the Grading System Program")

while True:
 print("Enter the mark of the student:")
 while True:
  s=eval(input("Enter mark (0-100): "))
  if 100>s>0:
     print("Entered mark: ", s)
     break
  else: print("Invalid mark")


 if 100>= s >= 80:
    print("Grade : A+")
 elif 80 > s >= 75:
    print("Grade : A")
 elif 75 > s >= 70:
    print("Grade : A-")
 elif 70 > s >= 65:
    print("Grade : B+")
 elif 65 > s >= 60:
    print("Grade : B")      
 elif 60 > s >= 55:
    print("Grade : B-")
 elif 55 > s >= 50:
    print("Grade : C+")
 elif 50 > s >= 45:
    print("Grade : C")
 elif 45 > s >= 40:
    print("Grade : D") 
 else:
    print("Fail")

 a=eval(input("Do you want to calculate for another student? (1 for Yes, 0 for No): "))
 if a == 0:
        print("Thank you for using the Grading System Program!")
        break
 elif a == 1:
    continue
 else: 
  print("Invalid input, exiting program.") 
 break   