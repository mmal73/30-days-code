# Day 2: Operators

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total = meal_cost
    total += meal_cost * (tip_percent/100)
    total += meal_cost * (tax_percent/100)
    print( round( total ) ) # int() function rounds down to the next integer

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
