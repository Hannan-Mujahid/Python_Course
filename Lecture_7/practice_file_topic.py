
# Create a new file "practice.txt", using python . Add the following data in it
"""
Hi everyone 
we are learning file I/O 
using python 
I like a programming language.
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
import os
with open("practice1.txt", "w") as f:
    f.write("Hi everyone \nwe are learning file I/O \nusing python \nI like a programming language.")
    with open("practice1.txt", "r") as f:
        print(f.read())
os.remove("practice1.txt")
