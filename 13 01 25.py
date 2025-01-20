from array import array

arr = array('i', [2, 0, 3, 0, 5, 6])

result = array('i')
zero_count = 0

for num in arr:
    if num == 0:
        zero_count += 1 
    else:
        result.append(num)  

result = array('i', [0] * zero_count) + result

print(result.tolist()) 