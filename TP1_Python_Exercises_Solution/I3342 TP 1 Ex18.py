# Remove all the characters other than integers from a string

string1 = 'I am 25 years and 10 months old'
print(f"string1 = {string1}")

# List comprehension
digit_string1 = "".join(char for char in string1 if char.isdigit())
print(f"the string after keeping only the digits: {digit_string1}")

# Expanded exaplanation
digit_string2 = ''
for char in string1:
    if char.isdigit():
        digit_string2 += char
print(f"the string after keeping only the digits: {digit_string2}")
