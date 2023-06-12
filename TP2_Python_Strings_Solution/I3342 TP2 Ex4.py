# Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple -
# you just need to sum all the digits of the date. If the result contains more than one digit, you 
# have to repeat the addition until you get exactly one digit. For example:
# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3
# 3 is the digit we searched for and found.
# Your task is to write a program which:
# asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or 
# MMDDYYYY - actually, the order of the digits doesn't matter)
# outputs the Digit of Life for the date.

# recursive approach
def digitoflife(string):
    digits = list(string.replace(" ", ""))
    digit_sum = 0
    for i in digits:
        digit_sum += int(i)   
    if len(string) == 0:
        return None
    if len(string) == 1:
        return string
    else:
        return digitoflife(str(digit_sum))
  
# iterative approach  
def digitoflife2(string):
    while len(string) > 1:
        string = str(sum(int(digit) for digit in string))
    
    return int(string)
        
print(digitoflife("20170101"))
print(digitoflife2("20170101"))