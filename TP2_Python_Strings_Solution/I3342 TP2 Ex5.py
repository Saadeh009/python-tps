# Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the 
# second being a combination of any characters.
# Your task is to write a program which answers the following question: are the characters 
# comprising the first string hidden inside the second string?
# For example:
# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are 
# neither the letters "d", "o", or "g", in this order)
# you should use the two-argument variants of the pos() functions inside your code;
# don't worry about case sensitivity.

# using string indices
def is_hidden1(string1, string2):
    index1 = 0
    index2 = 0
    while index1 < len(string1) and index2 < len(string2):
        if string1[index1].lower() == string2[index2].lower():
            index1 += 1
        index2 += 1
    return index1 == len(string1)

# using find() method     
def is_hidden2(word, text):
    word = word.lower()
    text = text.lower()
    pos = -1
    for letter in word:
        pos = text.find(letter, pos+1)
        if pos == -1:
            return False
    return True

print(is_hidden1("donor", "Nabuodonosor"))
print(is_hidden1("donut", "Nabuodonosor"))
print(is_hidden2("donor", "Nabuodonosor"))
print(is_hidden2("donut", "Nabuodonosor"))