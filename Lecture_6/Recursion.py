# Example of a simple recursive function to print numbers from n down to 1
"""
def show(n):
    if (n == 0):        #  base case
        return
    print(n)
    show(n-1)

show(5)
"""

# Example of a recursive function to calculate factorial of a number
"""
def fact(n):
    if (n == 1 or n==0):
        return 1
    return fact(n-1) * n

fact(6)
print(fact(6))
"""

# Example of a recursive function to calculate the sum of first n natural numbers
"""
def calculate_sum(n):
    if (n == 0):
        return 0
    # print(n)
    return calculate_sum(n-1) + n

sum = calculate_sum(10)    
print(sum)
"""
def sum(n):
    if (n == 0):
        return 0
    return sum (n+1) + n
print(sum(5))
