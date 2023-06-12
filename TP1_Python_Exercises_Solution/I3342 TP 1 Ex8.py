# Given two Python lists, iterate both lists simultaneously such that list1 should display items 
# in original order and list2 in reverse order

list1 = [i for i in range(1, 6)] # list of all numbers from 1 to 5
list2 = [i for i in range(6, 11)] # list of all numbers from 6 to 10

print(f"{list1} in order is: {list1}")
print(f"{list2} in reverse is: {list2[::-1]}")