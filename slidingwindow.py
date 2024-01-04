numbers = [7, 1, 2, 4, 5, 9, 7, 3, 1, 2]
k = 3
start = 0
pointer = 0
summation = sum(numbers[:k])  # Initial sum for the first window

for i in range(k, len(numbers)):
    summation = max(summation, sum(numbers[pointer+1:i+1]))
    pointer += 1

print(summation)
