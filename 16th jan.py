# 1. Find the Missing Number
# Given an array of n-1 numbers in the range 1 to n, find the missing number.
# Example:
# arr = [1, 2, 4, 5]
# Missing number is 3

arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
n = len(arr) + 1
total_sum = (n * (n + 1)) // 2
arr_sum = sum(arr)
missing_number = total_sum - arr_sum
print("Missing number is:", missing_number) # 2. Find the Duplicates
# Given an array where each number appears twice except one number, find the number that appears once.
# arr = [4, 3, 2, 7, 8, 2, 3]
# 4 and 7 are the numbers that appear once


arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
unique_numbers = []
for i in arr:
    if i not in unique_numbers:
        unique_numbers.append(i)
    else:
        unique_numbers.remove(i)
print("The numbers that appear once are:", unique_numbers)
# 3. Check if Array is Sorted
# Check whether a given array is sorted in ascending order.
# Example:
# arr = [1, 2, 3, 4]
# Output: True

arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
is_sorted = True  
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:  
        is_sorted = False  
        break  

print("Is the array sorted?", is_sorted) arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
n = len(arr)
if n == 0: 
    print("Array is empty")
else:
    majority_element = arr[0]  
    count = 1  

    for num in arr[1:]:  # Start the loop from the second element
        if num == majority_element:
            count += 1
        else:
            count -= 1

        if count == 0:
            majority_element = num #New candidate
            count=1 #new count

    print("The majority element is:", majority_element) # 5. Check for Balanced Array
# Given an array, check whether the sum of elements on the left is equal to the sum of elements on the right at any index.

# Example:
# arr = [1, 2, 3, 4, 10, 1, 2, 3]
# Output: True

arr = list(map(int, input("Enter the numbers separated by spaces: ").split()))
for i in range(1, len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i:])
    if left_sum == right_sum:
        print("Balanced array found at index", i)
        break
else:
    print("No balanced array found")#6. Find All Pairs in an Array that Sum to a Specific Target
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
