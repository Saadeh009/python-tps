# Write a python script to decide if a phrase/statement is palindrome

word = "radar"

if (word == word[::-1]):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")