#exersize five

dayNumber = int(input('Enter a number between 1 and 7: ')) #user inputs number

if(dayNumber == 1): #compares integer input to value and prints out day of the week
    print('Monday')
elif(dayNumber == 2):
    print('Tuesday')
elif(dayNumber == 3):
    print('Wednesday')
elif(dayNumber == 4):
    print('Thursday')
elif(dayNumber == 5):
    print('Friday')
elif(dayNumber == 6):
    print('Saturday')
elif(dayNumber == 7):
    print('Sunday')
else:
    print('error enter a number between 1 and 7') #prints out error if user enters anything other than numbers between 1 and 7