# Given a number count the total number of digits in a number

# Typecast to string approach
num1 = 123456789

print(f"number of digits in '{num1}' is: {len(str(num1))}")

# Mathematical approach
def count_digits(number):
    if number == 0:
        return 1  # Special case for 0
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count

num2 = 12345
digit_count = count_digits(num2)
print(f"number of digits in '{num2}' is: {digit_count}")