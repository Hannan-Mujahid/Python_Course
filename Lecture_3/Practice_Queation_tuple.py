#         Ek tuple banao jisme 5 numbers hon. Tuple ka naam numbers rakho.

#number = (1,2,3,4,5)

#        Tuple ka 3rd element print karo.

#print(number[2])

#        Tuple me "5" kitni baar aata hai, count karo.
'''
number = (1,2,3,4,5)
count = number.count(5)
print("Count of 5 in tuple:", count)
'''

#        Tuple me "7" kis index par hai, find karo.

'''
number = (1,2,3,4,5)
if 7 in number:
    print("7 is present in the tuple", number.index(7))
else:
    print("7 Tuple is not available in numbers. ")          
'''

#               Loop ke zariye har element ko print karo.
'''
number = (1,2,3,4,5)
for i in number:
    print(i)
'''

#            Tuple ko list me convert karo.
'''
number = (1,2,3,4,5)
list_number = list(number)
print("Tuple converted to list:", list_number)
'''


#            List ko wapas tuple me convert karo.

'''
number = (1,2,3,4,5)
list_number = list(number)
tuple_number = tuple(list_number)
print("Tuple converted to list:", list_number)
print("list converted to tuple:", tuple_number)
'''

#       Tuple ke first 3 elements ko slice karo.
'''
numbers = (1, 2, 3, 4, 5)
sliced_numbers = numbers[:3]
print("Sliced tuple (first 3 elements):", sliced_numbers)
'''

#       Tuple me koi new item add karne ki koshish karo. Kya error aata hai?
'''
numbers = (1, 2, 3, 4, 5)
numbers = numbers.append(6)
print("Tuple after trying to add an item:", numbers)
'''

#         Ek nested tuple banao:

nested_numbers = (1,2,3,(4,5,6))
print(nested_numbers[3])
print(nested_numbers[3][0])
print(nested_numbers[3][1])
print(nested_numbers[3][2])
print("Nested tuple:",nested_numbers)