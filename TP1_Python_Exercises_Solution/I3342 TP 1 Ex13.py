# Rename key city to location in the following dictionary

dict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
print(f"dict = {dict}")

dict["location"] = dict.pop("city") # pop() function returns the value of the selected key and deletes it from the dictionary

print("after renaming 'city' to 'location': ")
print(f"dict = {dict}")