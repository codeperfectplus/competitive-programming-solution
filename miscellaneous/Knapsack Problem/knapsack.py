def knapsack(profits, weights, max_capacity):
    
    total_profits = 0
    n = len(profits)

    ratios = [profits[i]/weights[i] for i in range(len(profits))]

    for i in range(n):
        for j in range(n-i-1):
            if ratios[j] < ratios[j+1]:
                ratios[j], ratios[j+1] = ratios[j+1], ratios[j]
                profits[j], profits[j+1] = profits[j+1], profits[j]
                weights[j], weights[j+1] = weights[j+1], weights[j]
    
    # knapsack algorithm using greedy approach

    for i in range(n):
        if weights[i] <= max_capacity:
            max_capacity -= weights[i]
            total_profits += profits[i]
        else:
            total_profits += profits[i] * (max_capacity/weights[i])
            break
            
            
    return total_profits
