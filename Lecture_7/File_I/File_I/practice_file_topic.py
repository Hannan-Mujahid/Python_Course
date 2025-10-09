
# WAP Create a new file "practice.txt", using python . Add the following data in it
"""
Hi everyone 
we are learning file I/O 
using python 
I like a programming language Python.
"""
# first Method
"""
f = open("practice.txt", "w" )
f.write("Hi everyone \nwe are learning file I/O \nusing python \nI like a programming language.")
f.close()
f = open("practice.txt", "r" )
print(f.read())
f.close()
"""
# second Method
"""
import os
with open("practice1.txt", "w") as f:
    f.write("Hi everyone \nwe are learning file I/O \nusing python \nI like a programming language.")
    with open("practice1.txt", "r") as f:
        print(f.read())
os.remove("practice1.txt")
"""

# WAP that replace occurrences of "Java" with "Python" in the file "practice.txt".
# first Method
"""
f = open("practice.txt", "r")
data = f.read()
new_data = data.replace("Python","Java")
print(new_data)
"""
# second Method
"""
with open("practice.txt", "r") as f:    
    data = f.read()
    new_data = data.replace("Python","Java")
    print(new_data)
   
    with open("practice.txt", "w") as f:
        f.write(new_data)
"""
# word = "learning"
"""
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find("learning" ) != -1):
        print("found") 
    else:
        print("not found") 
"""
