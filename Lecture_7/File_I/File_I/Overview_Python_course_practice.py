# 01
"""
n = int(input("Enter a number: "))
h = input("Enter a number: ")
sum = n + int(h)
print("The sum is: ", sum)
"""
# 02
"""
name = input("Enter your name: ")
age = int(input("Enter your age:"))
print("Hello! ", name ,"you are  ", age," years old.")
"""
# 03
"""
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit is: ", fahrenheit)
"""
# 04
"""
num = int(input("Enter a number: "))
if (num >= 1 ):
    print("The number is positive.", num)
elif(num < 1):
    print("The number is negative.", num)
else:
    print("The number is zero.", num)
"""
# 05
with open("Test_Python.txt","w") as f:
    f.write("23,45,67")
    with open("Test_Python.txt","r") as f:
        data = f.read()
        print(data)