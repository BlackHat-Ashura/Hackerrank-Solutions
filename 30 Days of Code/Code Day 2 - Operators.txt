def solve(meal_cost, tip_percent, tax_percent):
    meal_cost += meal_cost*(tip_percent + tax_percent)/100
    print(int(meal_cost + 0.5))