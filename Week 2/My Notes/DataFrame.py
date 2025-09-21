h="Hello, \nFucking World"
print(h)
import pandas as pd

# Creating a Python script to define a student dictionary
student = {
    'Name': ['Soumitro', 'Zihad', 'Shanto'],
    'ID': [1, 2, 3],
    'Phone Number': [24, 25, 25],
    'Blood Group': ['B+', 'B+', 'O+'],
    'Marks': [90, 85, 88]
}

sdf = pd.DataFrame(student)

print(sdf)

ss=sdf['Marks']

print("Printing Mark Series\n",ss)

#We can convert a Series into a DataFrame
#By selecting multiple columns (We need to use double square brackets)

ssds=sdf[['Marks', 'Name']]
print("Printing Mark and ID Series\nConverting Series into Data frame automatically\n", ssds)
