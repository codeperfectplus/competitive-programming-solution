def solve(meal_cost, tip_percent, tax_percent):
    answer = meal_cost + meal_cost * tip_percent / 100 + meal_cost * tax_percent / 100
    print(round(answer))
