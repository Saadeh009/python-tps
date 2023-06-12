# Display all duplicate items from a list

list1 = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicates = []
print(f"list1 = {list1}")

for element in list1:
    if list1.count(element) > 1 and element not in duplicates:
            duplicates.append(element)

print("List with only duplicates: ")
print(f"duplicates = {duplicates}")

# Note 
# duplicates2 = []
# duplicates2 = [element for element in list1 if list1.count(element) > 1 and element not in duplicates2]
# List comprehension in this case doesnt work, it returns [10, 20, 30, 10, 20, 30]
# To prevent this issue we can use the set() data structure and convert it to a list
# since the set doesn't allow duplicate items

duplicates2 = {}
duplicates2 = list({element for element in list1 if list1.count(element) > 1 and element not in duplicates2})
print(f"duplicates2 = {duplicates2}")