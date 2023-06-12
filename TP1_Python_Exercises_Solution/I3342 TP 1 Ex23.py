#  Given a list slice it into 3 equal chunks and reverse each chunk

list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(f"list1 = {list1}")

print(f"Chunk1 = {list1[:len(list1)//3][::-1]}")
print(f"Chunk2 = {list1[len(list1)//3:2*len(list1)//3][::-1]}")
print(f"Chunk3 = {list1[2*len(list1)//3:len(list1)][::-1]}")

# it can also be written by using an extra variable for better readability
chunk_size = len(list1)//3

print(f"Chunk1 = {list1[:chunk_size][::-1]}")
print(f"Chunk2 = {list1[chunk_size:2*chunk_size][::-1]}")
print(f"Chunk3 = {list1[2*chunk_size:len(list1)][::-1]}")