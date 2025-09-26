
# practice questions for break and continue

" break question "
"""
nums = [1,23,45,89,73,66,12,81,100,4,66]
i = 100
x = 0
while x< len(nums):
    if (nums[x] == i):
        print("found of idx",x)
        break
    else:
        print("Finding...")
    x += 1
print("Out of loop") 
"""


" break question "
"""
i = 1
while i<=10:
    if(i == 5):
        i += 1
        break
    print(i)
    i += 1
 """   


# continue question
'odd numbers from 1 to 10'
"""
i =1
while i<=10:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i +=1
"""

# continue question
'even numbers from 1 to 10'
"""
i =1
while i<=10:
    if i%2 != 0:
        i += 1
        continue
    print(i)
    i +=1
"""