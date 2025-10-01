#cricketer_name  = ["Babar Azam", "Virat Kohli", "Steve Smith", "Kane Williamson"]
#len(cricketer_name)
#print(len(cricketer_name))


#    WAF to print the length of a list . (list is the parameter)

"""
cricketer_name  = ["Babar Azam", "Virat Kohli", "Steve Smith", "Kane Williamson"]

def print_names(list):
    print("Total number of cricketers: ", len(list))

print_names(cricketer_name)
"""


# WAF to print the elements of a list in a single line . (list is the parameter)
"""
heroes = ["Superman", "Batman", "Wonder", "Flash",]

def print_hero(list):
    for hero in list:
        print(hero, end=", ")

print_hero(heroes)
"""

# WAF to find the factorial of a number. (number is the parameter)
# Factorial of 3 = 3*2*1 = 6

"""
n = 3
def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial of ", n, " is: ", fact)

calc_factorial(n)
"""


"""
def convertor(usd_val):   # function definition; parameter
    pkr = usd_val * 283     # 1 USD = 283 PKR
    print(usd_val, "PKR: ", pkr)        

convertor(100)    
"""

# WAF to find whether a number is even or odd. (number is the parameter)

"""
num = int(input("Enter a number: "))
def find_even_odd(num):
    if num % 2 == 0:
        print(num, "is an Even number.")
    else:
        print(num, "is an odd  number.")
    

find_even_odd(num)        
"""


# WAF to create a list of even and odd numbers. (number is the parameter)
"""
my_list = []
number= int(input("Enter a list of numbers: "))
def create_list(number):
    
    if number %2 ==0:
        print(number, "is an Even number.")
        my_list.append(number)
    else:
        print(number, "is an odd  number.")
        my_list.append(number)

create_list(number)
print("List of numbers: ", my_list)
"""

#  logic bna raha hu mind ma ak idea aa raha ha 


numbers_list = []

def create_list():
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(number, "is an Even number.")
        numbers_list.append(number)
    else:
        print(number, "is an odd  number.")
        numbers_list.append(number)

create_list()
print("List of numbers: ", numbers_list)
        
        