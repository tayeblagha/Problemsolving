import heapq

# Case 1: Basic Min Heap Operations
min_heap = []  # Initialize an empty list to represent the min heap

# Insert elements into the min heap
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 2)

print("Min Heap after insertion:", min_heap)

# Pop the minimum element from the min heap
min_element = heapq.heappop(min_heap)
print("Popped Min Element:", min_element)
print("Min Heap after popping:", min_heap)

# Case 2: Using a Min Heap for Sorting
unsorted_list = [5, 2, 9, 1, 5, 6]

heapq.heapify(unsorted_list)  # Convert the list into a min heap in-place

print(f"n largest: {heapq.nlargest(2, unsorted_list)}")
sorted_list = [heapq.heappop(unsorted_list) for _ in range(len(unsorted_list))]
print("Sorted List using Min Heap:", sorted_list)



# Case 3: Merge Sorted Lists using Min Heap
list1 = [1, 4, 7]
list2 = [2, 5, 8]
list3 = [3, 6, 9]

merged_list = list(heapq.merge(list1, list2, list3))
print("Merged Sorted List using Min Heap:", merged_list)

# # Case 4: Custom Objects in Min Heap
# class CustomObject:
#     def __init__(self, value):
#         self.value = value

#     # Implementing comparison methods for custom objects
#     def __lt__(self, other):
#         return self.value < other.value

#     def __eq__(self, other):
#         return self.value == other.value

# custom_objects_heap = []
# heapq.heappush(custom_objects_heap, CustomObject(10))
# heapq.heappush(custom_objects_heap, CustomObject(5))
# heapq.heappush(custom_objects_heap, CustomObject(8))

# print("Min Heap of Custom Objects:", [obj.value for obj in custom_objects_heap])
