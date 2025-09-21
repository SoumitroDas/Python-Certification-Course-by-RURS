h="Hello, \nF*cking World"
print(h)

print("Calculating the sum of the series 15+20+25+...+80\nUsing While loop")

n=80
s1=0
j=15
while j<=n:
 s1+=j
 j+=5

# Create the sequence string
sequence1 = ' + '.join(map(str, range(15, n+1,5)))
print(f"{sequence1} = {s1}")

print("Using for loops")

s2=0
for k in range(15,n+1,5):
 s2+=k

# Create the sequence string
sequence2 = ' + '.join(map(str, range(15, n+1, 5)))

print(f"{sequence2} = {s2}")