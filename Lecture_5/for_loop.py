"""
list = [1,2,3,4,5]
for num in list:
    print(num)
print(type(list))
"""


"""
nums = [1,4,9,16,25,49,64,81,100]
for char in nums:
    print(char)
"""


"""
nums = (1,4,9,16,25,49,64,81,100)
x = 81

idx = 0
for search in nums:
    print("finding....",)
    if (search == x):
        print("number found at idx :",idx)
    idx += 1
"""

# Basic For Loop Questions

"""
num = [1,2,3,4,5,6,7,8,9,10]

for el in num:
    print(el)
"""
# 1 se 20 tak ke even numbers print karo.
"""
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for x in list:
    if( x% 2 == 0):
     print(x)
print("Even numbers printed.....")    
"""
# 1 se 50 tak ke odd numbers print karo.
"""
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)
for n in numbers:
    if(n % 2 != 0):
        print(n)
print("Odd numbers printed.....")
"""    

# Ek string "python" ke har character ko for loop se print karo.
'''
string = "python"
idx = 0
for x in string:
    print(" idx",idx, "is",x)
    idx +=1
print("All characters printed.....")
'''

# Ek list fruits = ["apple", "banana", "mango", "orange"] ke sab elements print karo.
'''
fruits = ["apple", "banana", "mango", "orange"]
idx = 0
for fr in fruits:
    print(idx,fr)
    idx +=1
print("End program....")    
'''
#  2 ka table print karo.
'''
numbers =[1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    print("2 x",i,"=", 2*i)
'''

# User se ek number input lo aur us number ka table print karo.
"""
num = int(input("Enter a number to print its table: "))

numbers = (1,2,3,4,5,6,7,8,9,10)
for i in numbers:
    print(num,"x",i,"=",num*i)
"""

# Ek list [1, 2, 3, 4, 5] banao aur har element ka square print karo
"""
list = [1,2,3,4,5]
idx = 0
for el in list:
    print("Element square of idx",idx, "is",el*el)
    idx +=1
print("All elements printed.....")  
"""

# Ek list numbers = [10, 20, 30, 40, 50] banao aur sab numbers ka sum nikalne ke liye for loop use karo.

"""
numbers = [10, 20, 30, 40, 50]
total  = 0
for num in numbers:
    total += num

print("Total sum is :", total)
"""

# Ek list marks = [45, 67, 89, 34, 56] banao aur check karo kaun kaun se marks 50 se zyada hain.

"""
marks = [45, 67, 89, 34, 56]
num  = 50
for mark in marks:
    if mark >=num:
        print(mark,"is pass")
    else:
        print(mark,"is fail")
print("Result declared.....")
"""





 

