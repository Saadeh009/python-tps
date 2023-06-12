# Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

dict1.update(dict2)

print("after merging the two dictionatries: ")
print(f"dict1 = {dict1}")