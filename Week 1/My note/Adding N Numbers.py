h="Hello, \nFucking World"
print(h)

#Adding First n numbers using loop

n=eval(input("Enter how many number you want to add, starting from 1:(n) "))

s1=0
j=1
while j<=n:
 s1+=j
 j+=1

# Create the sequence string
sequence1 = ' + '.join(map(str, range(1, n+1)))
print(f"{sequence1} = {s1}")

print("Adding all Even numbers using for loops")

s2=0
for k in range(2,n+1,2):
 s2+=k

# Create the sequence string
sequence2 = ' + '.join(map(str, range(2, n+1, 2)))

print(f"{sequence2} = {s2}")