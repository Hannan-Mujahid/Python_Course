"""
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()
"""

"""
again_write = input("Do you want to write again (y/n): ")
if again_write == 'y':
    f = open("demo.txt", "a")
    data = input("Enter your data: ")
    f.write(data)
    f.write("\n")
f.close()
"""
"""
f = open("demo.txt", "a")
f.write("\nI'm learning Python and it's fun.")
f.close()
"""

# with open("demo1.txt", "x") as f:
#           f.write("I am Hannan Mujahid")

#           print(f.readline())
#           f.close()

"""
f = open("demo.txt", "w")
f.write("Hello, I'm Hannan Mujahid.\nI am learning Python.")
f = open("demo.txt", "r")
print(f.read())
f.close()
"""
"""
with open("demo_file.txt", "w") as f:
    f.write("this is a updated file.\n by Hannan mujahid")
    
import os 
os.remove("demo1.txt")
"""

f = open("practice.txt", "w")
f.write("Hi everyone \nwe are learning file I/O \nusing python \nI like a programming language.")
f.close()



