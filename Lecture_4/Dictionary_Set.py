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

student = {
    "name" : "Mr. Hannan ",
    "subject" : {
        "phy" : 34,
        "comp" : 45,
        "python" : 60
 }
}

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

new_Dict = {"Age" : 21 , "Day" : "Monday"}
student.update(new_Dict)
print(student)
student.update({"Age" : 21 })
print(student)




