#!bin/python3


from Employees import Employees #importing my own classes

e1 = Employees('Bryan', 'Sales', 'Director of Sales', 100000, 20)
e2 = Employees('Greg', 'Fruad', 'BSA 1', 80000, 10)

print(e1.name) #using methods from classes
print(e1.eligible_for_retirement())
