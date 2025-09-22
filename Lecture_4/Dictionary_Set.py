"""
dict = {
    "name" : "ali",
    "Subject" :  ["python","C++","java"],
    "topics" : ("dictionary","Sets"),
    "age" : 21,
    "city" : "karachi",
}
"""

"""
null_dict  = {}
null_dict["name"] = "hannan"
print(null_dict)
"""

"""
print(dict)
print(type(dict))
print(dict["Subject"])
print(dict["topics"])
print(dict["name"])
print(dict["age"])  
print(dict["city"]) 
"""
'''
student = {
    "name" : "Mr. Hannan ",
    "subject" : {
        "phy" : 34,
        "comp" : 45,
        "python" : 60
 }
}
'''
#               Dictionary Method in python

# nested dictionary
#print(student)
#print(student["subject"]["comp"])

#   myDict.key  Method in python
'''
print(list(student.keys()))
print(len(student))
'''

#    myDict.items Method in python
'''
print((student.items()))
print(list((student.items())))
pair = list((student.items()))
print(pair[1])
'''
#    myDict.get("key")    Method in python
'''
print(student["name1"])     # it will create error
print(student.get("name1"))  # no error but print None
'''
#      myDict.update("newDict")    Method in python
'''
new_Dict = {"Age" : 21 , "Day" : "Monday"}
student.update(new_Dict)
print(student)
student.update({"Age" : 21 })
print(student)
'''
'''
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

'''
collection = {1,2,3,4,"Hannan", "Ali", }
print(collection)
print(type (collection))
print(len(collection))
collection.add("Hello")
print(collection)

collection = set() # empty set; syntax
print(type(collection))
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
print(collection)
collection.clear()
print(collection)
print(len(collection))
collection1 = {1,2,3,4,5}
collection2 = {4,5,6,7,8}
print(collection1.union(collection2))
print(collection1.intersection(collection2))
