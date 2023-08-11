from array import *

'''
->An array is a fixed-size, contiguous block of memory that stores elements of the same data type.
Elements in an array are accessed using an index.
Python's built-in list is a dynamic array implementation that can grow or shrink as needed.

->Arrays have fast constant-time access to elements by index (O(1) time complexity),
but inserting or deleting elements in the middle of an array
can be expensive (O(n) time complexity) as other elements need to be shifted.

->Array is created in Python by importing array module to the python program.
Then, the array is declared as shown below −
'''
# Creating an array (Python list)


arr = [1, 2, 3, 4, 5]

# Accessing elements
# print(arr[0])  # Output: 1
# print(arr[2])  # Output: 3

'''UPDATING AN ARRAY'''
# arr[3] = 6
# print(arr[3])
# print(arr)
# # Length of the array
# length = len(arr)  # Output: 5
# print(f"length of the array is: {length}")



# array1 = array('i', [10,20,30,40,50])
'''INSERTING'''
# array1.insert(0,60)
# print(array1)
# for x in array1:
#    print(x)
#
# strings = ['hello', 'python', 'world']
# array2 = array('u')
#
# for string in strings:
#     array2.extend(string)  # Convert string to characters and add to the array
#
# for char in array2:
#     print(char)



'''all the arrays operations'''
#INSERTION
'''
#1 We can also create a blank array and can take the values for it from the user.
- First, we have to take the length of an array from the user. 
- input() function takes the value in the form of a string, so we have to change it into an integer using int().
- We can run a loop in a range of length of an array given by the user. At each iteration, we can take a value to be inserted in an array.
- append() is a function that is used to add a value or an element in an array.



#3
- index() function can also be used to get the index number of a value in an array.'''

#CREATING AN ARRAY FROM USER INPUT

user = array('i',[])

n = int(input("Enter the size of array :"))

for i in range(n):
   a= int(input("Enter the value :"))
   user.append(a)

print("The array by user is :",user)

search = int(input("Enter the value you want to search :"))

k=0

for j in user:
   if j == search:
      print(k)
      break
   else:
      k+=1

print(user.index(search))



'''Now we want to know that where the index is present of a certain value
#2
- To search for any value in an array or to check the index number at which the value is present, 
we need to increment the value of an iterator variable in every iteration.
- When the condition of comparison gets true, we stop the loop to iterate further 
and print the value of an iterator variable.
- The iterator variable will return an index number of the value, you have searched for.
'''


'''FOR DELETION WE USE :'''
user.remove([2])