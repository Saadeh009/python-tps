# Delete set of keys from a dictionary

dict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
print(f"dict = {dict}")

keysToRemove = ["name", "salary"]
for key in keysToRemove:
    if key in dict:
        del dict[key]
        
print("after removing the keys: ")
print(f"dict = {dict}")