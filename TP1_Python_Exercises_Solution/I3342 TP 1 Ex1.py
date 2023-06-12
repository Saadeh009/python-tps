# Given a list, iterate it, and display numbers divisible by five, and if you find a number 
# greater than 150, stop the loop iteration

list1 = [i for i in range(1, 201, 7)] # list of all numbers from 1 to 200 with a step of 7 [1, 8, 15, ...]
print(f"list1 = {list1}")

print("List of numbers in list1 divisible by 5: ")
for element in list1:
    if element > 150:
        print(f"{element} bigger than 150, loop will break.")
        break
    if element % 5 == 0:
        print(element)