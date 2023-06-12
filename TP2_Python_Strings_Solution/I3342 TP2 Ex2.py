# our task is to write a program which:
# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.
# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent;
# there are more than a few correct solutions - try to find more than one.

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string == "":
        print("Not a palindrome")
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
            
is_palindrome("Ten animals I slam in a net")
is_palindrome("Eleven animals I slam in a net")