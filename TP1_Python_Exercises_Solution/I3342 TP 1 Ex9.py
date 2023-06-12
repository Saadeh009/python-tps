# Given a Python list, remove all occurrence of 20 from the list

# List comprehension
list1 = [i for i in range(10, 41, 10) for j in range(3)] # list of numbers from 10 to 40 with a step of 10, each number appearing 3 times
print(f"list1 = {list1}")

list1 = [element for element in list1 if element != 20]
print("after removing all occurences of the number 20: ")
print(f"list1 = {list1}\n")

# while loop
list2 = [i for i in range(10, 41, 10) for j in range(3)]
print(f"list2 = {list2}")

while 20 in list2:
    list2.remove(20)
        
print("after removing all occurences of the number 20: ")
print(f"list2 = {list2}")