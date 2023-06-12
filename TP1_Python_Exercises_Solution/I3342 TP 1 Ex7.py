# Use a loop to display elements from a given list that are present at even index positions

list1 = [i for i in range(0, 11)] # list of all numbers from 1 to 10
print(f"list1 = {list1}")

print("elements at even index positions are: ")
for element in list1[::2]:
    print(f"index {list1.index(element)} = {element}")