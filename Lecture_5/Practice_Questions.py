# Question 1
"""
i = 1
while i<=100:
    print(i)
    i+=1
"""

# Question 2
"""
n = 100
while n>=1:
    print(n)
    n-=1
"""

# Question 3
"""
nums = [1,23,45,89,73,66,12,81,100,4]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1
"""

# Question 4
"""
nums = [1,23,45,89,73,66,12,81,100,4,66]
i = 66
n = 0
while n < len(nums):
    if (nums[n] == i):
        print("Found of  idx",n)    
    else:
        print("Finding....")
    n +=1
"""

"""
n = int(input("Enter a number to fine sum of n natural numbers: "))
sum = 0
for i in range(1,n+1):
    sum +=i

print("total sum = ",sum)
"""

# WAP to find  the sum  of first n numbers. (Using while loop)
"""
n = int(input("Enter a number to find natural: "))
sum = 0
i=1
while i <=n:
    sum +=i
    i +=1
    print("total sum = ",sum)
"""


 # WAP to find the factorial of a number. (Using for loop)
"""
n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1,n+1):
        fact = fact * i
        i +=1
print("Factorial of ",n," is ",fact)
"""




