# print("Hi hannan." "how are you")

# name= "ali raza"
# age = 21
# gender= "Male"

# 'print(name)'
# 'print(age)'

# print("What's your name", name)
# print("What's your age", age)
# print(type(name))



# list topic in python

# list = [1,2,3,4,5,6,7,8,9]
# print(list)
# print(list[0])
# print(list[-1])
# print(list[-2])
# print(list[-6])

# marks = [2.5, 3.5, 4.5, 5.5, 6.5]
# print(marks)
# print(type(marks))
# print(len(marks))

# list= [1,2,3,4,5,1,6,7,1,8,9]
# list.append(500)
# print(list)
# print(len(list))
# list.sort(reverse = True)
# print(list)
# print(len(list))
# list.remove(500)
# print(list)
# print(len(list))
# list.insert(2, 300)
# print(list)
# print(len(list))
# list.reverse()
# print(list)
# print(len(list))
# list.insert(1, 100)
# print(list)
# print(len(list))
# list.remove(100)
# print(list)
# print(len(list))
# list.remove(1)
# print(list)
# print(len(list))
# list.pop(8)
# print(list)
# print(len(list))
# list.copy()
# print(list)
# print(len(list))




#  Tuple topic in python
# tuple = (1,2,3,4,5,6,7,4,2,8,9)
# print(type(tuple))
# print(tuple) 
# print(len(tuple)) 

# print(tuple.index(5))  
# tuple.count(5)
# print(tuple.count(4))



#    WAP to ask ther user to enter name of the favorite movies & store them in list

# movies = []
# name_1 = input("enter the first movie name:" )
# name_2 = input("enter the second movie name:" )
# name_3 = input("enter the third movie name:" )
# movies.append(name_1)
# movies.append(name_2)
# movies.append(name_3)   
# print(movies)









# list = [1,2,1]
# copy_list1 = list.copy()
# copy_list1.reverse()
# if( copy_list1 == list ):
#     print("palindrome")
# else:
#     print("not palindrome")


# grade = ["c","d","d","a","a","b","b","d","a"]
# grade.sort()
# print(grade) 




# lecture 4





# dict = {
#     "name" : "Han", "age" : 23 , "subject" : ["python", "C++", "java" ]
#     }
# dict["name"] = "ali"
# print(dict["name"])
# dict["age"] = "34"
# print(dict["age"])
# dict["subject"] = input("Enter your subject Author name: ",)






student = {
    "Name" : "Ali Raza", 
    "Age" : 21, 
    "Subject" : {"Phy": 67, "Comp" : 78, "Eng" : 45, "Urdu" : 66}
}
print(student)
print(student["Subject"]["Phy"])
print(student.keys())
print(len(student))
student["Subject"]["Phy"] = 87
# Answer kya ho ga ...?
print(student["Subject"]["Phy"])

print(student.keys())
print(student.values())
print(student.items())
# print(list(student.keys())) 
print(list(student.values())) 
print(list(student.items()))
print(student.get("Name"))
print(student.get("Subject"))


