# Get the key of a minimum value from the following dictionary

dict1 = {'Physics': 82, 'Math': 65, 'History': 75}
print(f"dict1 = {dict1}")

min_key = min(dict1, key=dict1.get) # key=dict1.get so the min() function reads the values and not the keys
# key = dict1.get instructs the min function to compare the value of dict1 not the keys

print(f"The key of minimum value in dict1 is: {min_key}")
