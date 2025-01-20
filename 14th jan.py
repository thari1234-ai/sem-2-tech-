14.1.25 
 
Technical home task 
 
 
gas = list(map(int, input().split())) 
cost = list(map(int, input().split())) 
 
total_gas = sum(gas) 
total_cost = sum(cost) 
if total_gas < total_cost: 
    print(-1) 
else: 
    current_gas = 0 
    starting_point = 0 
 
    for i in range(len(gas)): 
        current_gas=current_gas+gas[i]-cost[i] 
        if current_gas < 0:                    
            starting_point = i + 1           
            current_gas = 0 
 
    print(starting_point) 
 
 
 
 
2. 
 
ratings = list(map(int,input("enter no ofchild:").split())) 
n = len(ratings) 
candies = [1] * n 
for i in range(1, n): 
    if ratings[i] > ratings[i - 1]: 
        candies[i] = candies[i - 1] + 1 
for i in range(n - 2, -1, -1): 
    if ratings[i] > ratings[i + 1]: 
        candies[i] = max(candies[i], candies[i + 1] + 1) 
total_candies = sum(candies) 
print("Total candies needed:", total_candies) 