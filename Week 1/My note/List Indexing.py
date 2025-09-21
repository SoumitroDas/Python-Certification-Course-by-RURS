my_list = [10, 20, 30, 40, 50, 'apple', "banana", 'cherry', True, 4+5j]


print(my_list[0])           # first element
print(my_list[-1])        # last element
print(my_list[2:5])       # elements from index 2 to 4
print(my_list[2:9:3])  # elements from index 2 to 8, step 3
print(my_list[-9:-2])   # from index -9 to -3
print(my_list[5:])         # from index 5 to the end
print(my_list[:5])         # from the start to index 4
print(my_list[::2])        # every second element
print(my_list[::-1])       # reverse the list

#find length etc

lst = [1,9,1,0,8,2,8,1,4,9]
print(len(lst))
print(sum(lst))
print(max(lst))
print(min(lst))
print(lst*3)


#change list

ls1 = ["a", "b", "c", "m", "o"]
print(ls1 + ["x", "y", "z"])  # concatenate lists
print(ls1 * 2)                # repeat the list

ls1[-4]= 10
print(ls1)                

ls=ls1
print(ls)

ls1.clear()  # clear the list
print(ls1)  # now ls1 is empty

ls2 = ["apple", "banana", "cherry", "apple", "cherry", "apple"]
print(ls2.count("apple"))  # how many times

print(ls2.index("banana"))  # index of first occurrence
ls2.append("orange")  # add to the end
print(ls2)

fruits = ['apple', 'banana', 'cherry']
flowers = ['rose', 'sunflower', 'lotus']

fruits.extend(flowers)  # Add all elements of 'flowers' to the end of 'fruits'
print(fruits)

ls3 = ['apple', 'banana', 'cherry', 'rose', 'sunflower', 'lotus']

ls3.insert(3, "mango")  # Insert "mango" at index 3 permanently
print(ls3)               # Print the updated list
print(len(ls3))          # Print the length of the list
ls3.insert(-4, "kiwi")  # Insert "kiwi" at index -4
print(ls3)               # Print the updated list again

ls3.remove("cherry")   # Removes "cherry" from the list
print(ls3)             # Print the updated list
ls3.pop(4)   # remove element of 4th index
print(ls3)

ls3.reverse()
print(ls3)

ls3.sort() # sort in ascending order
print(ls3) # sort alphabeticaly. Capital letter first

ls3.sort(reverse=True) # sort in descending order
print(ls3)

print(ls3[3][2])  # Access the 3rd character of the 4th element in the list

#2D
A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

for row in A:
  print(row)