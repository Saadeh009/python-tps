# Write a function func1() such that it can accept a variable length of argument and print all 
# arguments value

def func1(*args):
    print(f"func1{args}:")
    for arg in args:
        print(arg)
    print("\n")

# Example usage
func1(20, 40, 60)
func1('abc', 40, 60, 10, [1, 2, 3])