
"""     Lists in Python

marks = [90.2,23.8,45.6,78.9,100.0,67.5]
# Print the list
print(marks)
# Print the type of the list
print(type(marks))
# Print the first element of the list
print(marks[0])
# Print the last element of the list
print(marks[-1])
# Print the first three elements of the list
print(marks[:3])
# Print the last three elements of the list
print(marks[-3:])
# Print the elements from index 1 to 3
print(marks[1:4])

"""

       #  Mutable List in python 
"""
name = ["ali,ahmad,sara,mahmood"] 
print(name)
name[0] = "hannan"
print(name[0])
""" 
"""
Ask the user for the index where they want to insert the name

index = int(input("Enter the index where you want to insert the name: "))
new_name = input("Enter name: ")
name[index] = new_name
print(name)
"""
           # list Slicing in python
"""          
marks =  [34,45,23,56,23] 
print(marks[1:4])  # [45, 23, 56]
print(marks[:3])   # [34, 45, 23]       
print(marks[2:])   # [23, 56, 23]
print(marks[-3:-1])  # [23, 56, ]      
"""


       # list Methods in python

list = [1,2,3,4,5,6,7,8,9]
list.append(12)
print(list)

list = ['a','f','c','b','d','e']
#list = sort(list)
print(list.sort())
print(list)


list = [1,3,5,6,7,2,9,8,4,10]
print(list.sort(reverse=True))
print(list)

list = [1,3,5,6,7,2,9,8,4,10]
print(list.reverse())
print(list)


list = [1,3,5,]
print(list.insert(2,10))
print(list)

list = [1,3,5,]
print(list.pop(2))
print(list)
