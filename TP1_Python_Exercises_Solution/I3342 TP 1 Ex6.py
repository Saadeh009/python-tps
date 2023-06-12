# Print the following pattern: 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

size = 5

print(f"pattern for size {size}: \n")
for i in range(1, size+1):
    print("* " * i)
for i in range(size-1, 0, -1):
    print("* " * i)