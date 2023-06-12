# Write a program to display all prime numbers within a range

start = 1
end = 20

print(f"prime numbers between {start} and {end} are: ")

for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num/2)+1): 
            if (num % i) == 0:
                break
        else:
            print(num)