# Filter dictionary to contain keys present in the given list

dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
print(f"dict = {dict}")

filter_keys = ['A', 'C', 'F']

filtered_dict = {key: value for key, value in dict.items() if key in filter_keys}

print("after removing the keys: ")
print(f"filtered_dict = {filtered_dict}")