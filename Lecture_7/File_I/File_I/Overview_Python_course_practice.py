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

marks_1 = int(input("Enter number of subject english: "))
marks_2 = int(input("Enter number of subject math: "))
marks_3 = int(input("Enter number of subject computer: "))
marks_4 = int(input("Enter number of subject science: "))
if marks_1 and marks_2 and marks_3 and marks_4 >= 80:
    print(marks_1,"Grade A")
elif marks_1 and marks_2 and marks_3 and marks_4 >= 70:
    print(marks_2,"Grade B")
elif marks_1 and marks_2 and marks_3 and marks_4 >= 60:
    print(marks_3,"Grade C")
elif marks_1 and marks_2 and marks_3 and marks_4 >= 50:
        print(marks_4,"Grade D")
else:
    print("Grade D is fail")
