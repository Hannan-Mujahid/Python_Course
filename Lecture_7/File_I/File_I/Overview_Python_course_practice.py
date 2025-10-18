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

"""
with open("Test_Python.txt","w") as f:
    f.write("23,45,67")

def find_biggest_num():
    with open("Test_Python.txt","r") as f:
            data = f.read()
            print(data)
            num_list = data.split(",")
            number = int(num_list[0])
            for n in num_list:
                if int(n) > number:
                     number = int(n)
            print("The biggest number is: ", number)

find_biggest_num()
"""
# 06
"""
enter_user = int(input("Enter a number: "))
if enter_user %2 ==0:
    print("The number is even.")
else:
    print("The number is odd.")
"""
# 07
# Ek student ke marks input lo aur uske hisaab se grade print karo (A, B, C, D, F).
"""
# Input from user
obtained = float(input("Enter obtained marks: "))
total = float(input("Enter total marks: "))

# Calculate percentage
percentage = (obtained / total) * 100
print("Percentage:", percentage)

# Determine grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
"""
# 08
# 1 se 5 tak numbers print karo using for loop.
"""
n = 5
for i in range(1, n+1):
    print(i)
"""
# 09
# 1 se 20 tak ke even numbers print karo.
"""
n = 20
for i in range(1,n+1):
    if i%2 == 0:
        print("Even number:", i)
"""    
# 10
# 1 se 50 tak ke odd numbers print karo.
"""
n = 50
for i in range(1,n+1):
    if i%2 != 0:
        print("Odd number:",i)
"""
# 11
# 5 ka table print karo using for loop.
"""
num = int(input("Enter a number to print its table: "))
for i in range(1,11):
    print(num,"x", i ,"= ",num*i)
"""
# 12
# Numbers = [10, 20, 30, 40, 50] — in sab ka sum find karo using loop.
"""
numbers = [10, 20, 30, 40, 50]
idx = 0
for i in numbers:
    idx += i
    print(idx)
"""
numbers = [10,20,30,40,50]
idx = 0
for i in numbers:
    idx += i
    print(idx)
 





    