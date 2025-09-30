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