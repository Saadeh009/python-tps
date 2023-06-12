# You already know how split() works. Now we want you to prove it.
# Your task is to write your own function, which behaves almost exactly like the 
# original split() method, i.e.:
# -it should accept exactly one argument - a string;
# -it should return a list of words created from the string, divided in the places where 
# the string contains whitespaces;
# -if the string is empty, the function should return an empty list;

def mysplit(string):
    if string == "":
        return []
    else:
        words = []
        word = ""
        for char in string:
            if char.isspace():
                if word != "":
                    words.append(word)
                    word = ""
            else:
                word += char
        if word != "":
            words.append(word)
        return words

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit(" "))
print(mysplit(" abc "))
print(mysplit(""))