
"""
def calc_sum(a,b):  # Function Definition
    sum = a + b
    print("Sum is: ",sum)
    return sum

calc_sum(5,10)      # Function Call 
# more lines of code


calc_sum(15,25)
# more lines of code

calc_sum(100,250)
"""
"""
def calc_sum(a,b):      # Function Definition; parameters
    return a + b

sum = calc_sum(5,10)      # Function Call; arguments
print("Sum is: ",sum)
"""
"""
def print_hello():
    print("Hello")
    
out_put = print_hello()
print(out_put)
"""

"""
def calc_aveg(a,b,c):
    sum = a+b+c 
    average = sum / 3
    print("Sum is: ",sum)
    print("Average is: ",average)

calc_aveg(5,10,15)
print("More lines of code")
calc_aveg(20,30,40)
"""


def calc_aveg(a,b,c):
    sum = a+b+c 
    average = sum / 3
    return sum, average

out_sum, out_avg = calc_aveg(5,10,15)
print("Sum is: ",out_sum)


