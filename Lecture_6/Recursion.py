# Example of a simple recursive function to print numbers from n down to 1
"""
def show(n):
    if (n == 0):        #  base case
        return
    print(n)
    show(n-1)

show(5)
"""


def fact(n):
    if (n == 1 or n==0):
        return 1
    return fact(n-1) * n

fact(6)
print(fact(6))