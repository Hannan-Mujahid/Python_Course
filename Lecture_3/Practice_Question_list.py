
                # First: Practice_Question.py
"""
movies = []
name_1 = input("Enter first movie name: ")
name_2 = input("Enter second movie name: ")
name_3 = input("Enter third movie name: ")

movies.append(name_1)
movies.append(name_2)
movies.append(name_3)
print(movies)
"""

#                # Second: Tuple_in_python_Immutable.py

"""
list1 = [1,2,3]
list2 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

if (copy_list1 == list1):
    print("palindrome")
else:
    print("Not Palindrome")    

if (copy_list2 == list2):
    print("palindrome")
else:
    print("Not Palindrome")
"""    


#                # Third: Tuple_in_python_Immutable.py
""" 
grade_1 = ("C","D","D","A","A","B","B","A")
grade_1 = grade_1.count("A")
print(grade_1)
""" 

#                # Fourth: Tuple_in_python_Immutable.py
"""
list_1 = ["C","D","D","A","A","B","B","A"]
list_1 = list_1.sort()
print(list_1)
"""

"""
fruit = ["APPLE","MANGO","ORANGE","GRAPES","PINEAPPLE"]
print(fruit[1])
fruit.append("BANANA")
print(fruit)
fruit[0] = "challi"
print(fruit)
"""
"""
fruit = ["APPLE","MANGO","ORANGE","GRAPES","PINEAPPLE"]
if "MANGO" in fruit:
    print("Mango is present in the list")
else:
    print("Mango is not present in ths list")   
"""
"""
fruit = ["APPLE","MANGO","ORANGE","GRAPES","PINEAPPLE"]
fruit.remove("PINEAPPLE")
print(fruit)
"""
#           # first element ko reverse ma print karna ha
"""
fruit = ["APPLE","MANGO","ORANGE","GRAPES","PINEAPPLE"]
fruit[0] = fruit[0][::-1]
print(fruit)
"""

#           # All element ko reverse ma print karna ha

"""
fruit = ["APPLE","MANGO","ORANGE","GRAPES","PINEAPPLE"]
for i in range(len(fruit)):
    fruit[i] = fruit[i][::-1]
    print(fruit[i])
"""    

#          First element ko sort karna ha ascending order ma
'''
fruit = ["APPLE","MANGO","ORANGE","GRAPES","PINEAPPLE"]
fruit[0] = sorted(fruit[0])
#print(fruit[0])
print(fruit)
'''
#          list ko merge karna ha
'''
list_2 = ["APPLE","MANGO","ORANGE"]
list_1 = ["GRAPES","PINEAPPLE"]
merge_list = list_1 + list_2
print(merge_list)
'''

#            list ko print karo for loop k sat

"""
fruit = ["APPLE","MANGO","ORANGE","GRAPES","PINEAPPLE"]
for fruit in fruit:
    print(fruit)
"""
