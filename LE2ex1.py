#Exersize one
purchase = float(input('Enter the amount of the purchase: '))


salesTax = purchase*0.05 #compures the states sales tax
countyTax = purchase*0.025 #computes the county sales tax

print('\nThe purchase amount is', format(purchase,'.2f')) #display purschase amount
print('The sales tax is', format(salesTax,'.2f')) #display state sales tax
print('The county tax is', format(countyTax,'.2f')) #display county sales tax
print('The total is', format(purchase + salesTax + countyTax, '.2f')) #display the total sales tax 