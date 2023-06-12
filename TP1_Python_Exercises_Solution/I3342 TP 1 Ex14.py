# Reverse the following tuple

tuple1 = (10, 20, 30, 40, 50)
print(f"tuple = {tuple1}")

tuple1 = tuple1[::-1]

print("after reversing the tuple: ")
print(f"tuple = {tuple1}")

# Note:
# Tuples in python are immutable, which means we cannot change elements directly
# we cannot do tuple1[0] = 60 or use remove() or append() on tuples
# but by doing tuple1 = tuple1[::-1] we are overriding the tuple1 in memory and creating
# a new one, not changing its elements directly
# we can also do tuple1 = tuple(reversed(tuple1)), the reversed() function returns an iterable object
# and we convert it to a tuple by using the tuple() function