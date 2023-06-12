# Find all occurrences of “USA” in a given string ignoring whether it is capitalized or not

string1 = "Welcome to USA. usa is awesome, isn't it?"
sub_string = "USA"
print(f"string1 = {string1}")

# to count the number of occurences
nb_of_occurences = string1.lower().count(sub_string.lower())
print(f"'{sub_string}' appears {nb_of_occurences} times in the string")

# to know at what index is each occurence
string1 = string1.lower()
sub_string = sub_string.lower()

indices_of_occurrence = []
start = 0
while True:
    start = string1.find(sub_string, start)
    if start == -1:
        break
    indices_of_occurrence.append(start)
    start += len(sub_string)

print(f"The occurrences of '{sub_string}' in the string are at: {indices_of_occurrence}")