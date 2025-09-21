h="Hello, \nF*cking World"
print(h)

#Sum of all odd numbers from 1 to 100

n=100

s=0
j=1
while j<=n:
 s+=j
 j+=2

# Create the sequence string
sequence = ' + '.join(map(str, range(1, n+1,2)))
print(f"{sequence} = {s}")
