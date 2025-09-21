h="Hello, \nFucking World"
print(h)

#Result Calculation Program

print("Welcome to the Result Calculation Program")
print("Enter the marks of the first student:")
sub1=eval(input("Mark of Mathematics: "))

sub2=eval(input("Mark of Physics: "))
  
sub3=eval(input("Mark of Chemestry: "))

sub4=eval(input("Mark of Biology: "))

sub5=eval(input("Mark of Practical: "))

print("Marks of Mathematics: ", sub1)
print("Marks of Physics: ", sub2)
print("Marks of Chemistry: ", sub3)
print("Marks of Biology: ", sub4)
print("Marks of Practical: ", sub5)

total = sub1 + sub2 + sub3 + sub4 + sub5
print("Total Marks:", total)

Avg= (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print("Average Marks:", Avg)

if Avg > 80:
    print("Result = First Class")
elif Avg > 50:
    print("Result = Second Class")
elif Avg > 30:
    print("Result = Third Class")
else:
    print("Result = Fail")
