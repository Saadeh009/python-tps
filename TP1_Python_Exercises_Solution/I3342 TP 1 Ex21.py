# Given two lists create a third list by picking odd index elements from the first list and 
# even index elements from the second.

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
print(f"list1[] = {list1} (odd index element list)")
print(f"list2[] = {list2} (even index element list)")

list3 = [list1[i] for i in range(1, len(list1), 2)] + [list2[j] for j in range(0, len(list2), 2)]
print(f"list3[] = {list3}")