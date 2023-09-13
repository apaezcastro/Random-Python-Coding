#exersize three
mealCost = float(input('Enter the menu price of your meal: '))

tip = mealCost*0.18 #calculates tip
salesTax = mealCost*.07 #calculates sales tax

print(format(tip,'.2f')) #output tip
print(format(salesTax,'.2f')) #output sales tax
print(format(mealCost + tip + salesTax,'.2f')) #output total