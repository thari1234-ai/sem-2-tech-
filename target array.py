#6. Find All Pairs in an Array that Sum to a Specific Target
#Given an array of integers and a target sum, find all pairs of numbers that sum up to the target.

#Example:
#arr = [2, 4, 3, 5, 7, 8]
#target = 10
# Output: [(2, 8), (3, 7)]

arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
target = int(input("Enter the target sum: "))
pairs = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))
print("Pairs that sum to the target are:", pairs)
