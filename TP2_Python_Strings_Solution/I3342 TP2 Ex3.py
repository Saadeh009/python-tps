# An anagram is a new word formed by rearranging the letters of a word, using all the original 
# letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, 
# while "I am" and "You are" are not.
# Your task is to write a program which:
# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

def is_anagram (string1, string2):
    if string1 == "" and string2 == "":
        print("Not anagrams")
    else:
        if sorted(string1.replace(" ", "").lower()) == sorted(string2.replace(" ", "").lower()):
            print("Anagrams")
        else:
            print("Not anagrams")

is_anagram("Listen", "Silent")
is_anagram("Modern", "Norman")