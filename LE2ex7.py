#exersize seven

age = int(input('Enter the persons age: ')) #user inputs persons age

#calcuates category of persons age and ouputs what category the person falls into.
if(age <= 1):
    print('This person is an infant')
elif(13 > age > 1):
    print('This person is a child')
elif(13 >= age or age < 20):
    print('This person is a teenager')
else:
    print('This person is an adult')