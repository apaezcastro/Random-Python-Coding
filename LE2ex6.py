#exersize six

#takes input of rectangles length and width from user
width1 = int(input('Enter the width of the first rectangle: ')) 

length1 = int(input('Enter the length of the first rectangle: '))

width2 = int(input('Enter the width of the second rectangle: '))

length2 = int(input('Enter the length of the second rectangle: '))

#calculates the area of both rectangles
area1 = width1*length1

area2 = width2*length2

#outputs which rectnagle has the greater are or if they are the same
if(area1 > area2):
    print('The first rectangle has the greater area.')
elif(area1 < area2):
    print('The second rectangle has the greater area.')
else:
    print('both rectangles have the same area.')