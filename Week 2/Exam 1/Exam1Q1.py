'''Question 01:
1) A list subject containing: Bangla, English, Math.
2) Add a new element: ‘ICT’ in the list and print the list
3) Add the elements of the list science=[‘Physics’, ‘Chemistry’,
‘Math’, ‘Biology’] in subject and print the list
4) Add ‘Higher Math’ in index 5 and print the list
5) Count the number of ‘Math’ in the list
6) Remove the item ‘Chemistry’ from the list and print the list
7) Remove the item of index 4 in the list and print the list
8) Reverse the list elements
9) Sort the elements in ascending order
10) Sort the elements in descending order   '''
h="Hello, \nFucking World"
print(h)

print("Question 01: 1")
sub=["Bangla", "English", "Math"]

print("Question 01: 2 ")
sub.append("ICT")
print(sub)

print("Question 01: 3")
science = ['Physics', 'Chemistry', 'Math', 'Biology']
sub.extend(science)

print(sub)

print("Question 01: 4")
sub.insert(5, "Higher Math")
print(sub)

print("Question 01: 5")
cm = sub.count("Math")  
print("Number of elements of 'Math' in the list:", cm)

print("Question 01: 6")
sub.remove("Chemistry")
print(sub)

print("Question 01: 7")
sub.pop(4)
print(sub)

print("Question 01: 8")
sub.reverse()
print(sub)

print("Question 01: 9")
sub.sort()
print(sub)

print("Question 01: 10")
sub.sort(reverse=True) 
print(sub)