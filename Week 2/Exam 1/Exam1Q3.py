'''Question 03:
 Create a python program to calculate the sum of the series
13+17+21+25+29+………..+82
'''
h="Hello, \nF*cking World"
print(h)

#Sum of 13+17+21+25+29+………..+82

n=82

s=0
j=13
while j<=n:
 s+=j
 j+=4

# Create the sequence string
sequence = ' + '.join(map(str, range(13, n+1,4)))
print(f"{sequence} = {s}")
