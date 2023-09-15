#!/bin/python3
#how to read and write files

months = open('months.txt') #open files

for month in months: #goes through each item in the list
    print(month.strip())
months.close() #closes file

days = open('days.txt', 'w') #puts open in write mode

days.write('Monday') #writes to a file

days.write('\nTuesday') #overwrites file unless we run append as in this case on the end

days.close() #best practice close file

days = open('days.txt', 'a') #appends the file

days.write('\nMonday\nTuesday\nWednesday')

days.close()
