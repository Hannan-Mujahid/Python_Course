
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
# without function
"""
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find("learning" ) != -1):
        print("found") 
    else:
        print("not found") 
"""
# Code write with function
"""
def check_word_in_file():
    with open("practice.txt", "r") as f:
        data = f.read()
    if (data.find("learning" ) != -1):
        print("found") 
    else:
        print("not found")
check_word_in_file()
"""

# WAP to find the line number of the line containing the word "learning" in the file "practice.txt".
"""
def check_for_line_in_file():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
       while data:
            data = f.readline()
            if (word in data):
                   print("line no")
                   return
            line_no += 1
    return -1        
  
print(check_for_line_in_file())      
"""

# WAP to count the number of even numbers from a list of numbers stored in a file "practice_2.txt" (numbers are separated by comma)
"""
count = 0
with open("practice_2.txt", "r") as f:
    data = f.read()
    # print(data)

    # num = ""
    # for i in range(len(data)):
    #     if (data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
    nums = data.split(",")
    print(nums)
    for val in nums:
        if (int(val) %2 != 0):
            print(int(val))
            count += 1
print("Total count of odd number", count)
  """  

    

    