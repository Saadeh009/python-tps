# Arrange a string of characters such that lowercase letters should come first

string1 = "FeDcBa"
print(f"string1 = {string1}")

uppercase_letters = []
lowercase_letters = []

for char in string1:
    if char.isupper():
        uppercase_letters.append(char)
    else:
        lowercase_letters.append(char)

sorted_string = "".join(lowercase_letters + uppercase_letters) # convert the list to a string using join()

print(f"sorted_string = {sorted_string}")

# Note:
# if we use the sorted() function, it returns a list of the letters sorted by ASCII code
# in this case sorted(string1) returns ['B', 'D', 'F', 'a', 'c', 'e']