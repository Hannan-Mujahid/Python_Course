# Question 1
'''
dict = {"table": ["a piece of furniture"," list of fact & figures"],
         "cat": "a small animal"}
print(dict)
print(type(dict))
'''

# Question 2
'''
subjects = {
    "python", "java", "c++", "javascript", "python", "java", "c++", "python", "java", "c"
}
print(subjects)
print(len(subjects))
print(type(subjects))
'''
# Question 3
# Method 1
"""
subjects_name = {}
for i in range(3):
    name = input("Enter your subject name: ")
    subjects_name[name] = int(input("Enter your marks: ")) 
"""
# Method 2
"""
subjects = {}
x = int(input("Enter number of subject English:"))
subjects["English"] = x
print(subjects)
y = int(input("Enter number of subject math:"))
subjects["math"] = y
print(subjects)
z = int(input("Enter number of subject comp:"))
subjects["comp"] = z
print(subjects)
print(type(subjects))
"""

# Method 3 watch on youtube 
"""
marks = {}
x = int(input("enter number of subject english: "))
marks.update({"english": x})
y = int(input("enter number of subject math: "))
marks.update({"math": y})
z = int(input("enter number of subject comp: "))
marks.update({"comp": z})
print(marks)
print(type(marks))
"""
# Question 4
# Method 1
"""
values = {
    "int": 5,
    "float": 5.5,
}
print(values)
"""
# Method 2
"""
values = {5, 5.0}
print(values)
"""