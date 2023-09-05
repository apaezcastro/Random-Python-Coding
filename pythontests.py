# this is gonna be for more notes other than math which contains all kinds of notes

def nl(): # this prints out a new line in fewer characters
    print('\n')
nl()

#LISTS - Have brackets [] inside lists are items

movies = ['In Brudge', 'Inglorious Basterds', 'John Wick']
carla_movies = ['Star Wars', 'John Wick']
print(movies[1]) #returnes second item in list
print(movies[0]) #returns 1st item in list
print(movies[0:2]) # returnes first item listed, butand goes up to the last one but does not print it
print(movies[:1])
print(movies[2:])
nl()
nl()
#methods for lists .pop() empty removes last, .append(), .insert() 
def lastmovieinlist(): #this fun this function removes last element from list and returns it
    lastmv = movies.pop()
    return lastmv

movies.insert(0, lastmovieinlist()) #this puts john wick at the front
print(movies)
#list can also be concatenated
print(movies + carla_movies)
ourmovies = movies + carla_movies
print(ourmovies)
print(movies + ['lol'])
# also can do lists inside of lists 2d lists

# for loops

for x in movies:
    print(x)

nl()

# advanced strings
#link tuples, strings are imputible call elements of string with indexing

sentence = '          This is a sentence    '
print(sentence[:4])
print(sentence.split()) #delimiter
print(sentence.strip())

print(type('a' in 'apple'))
nl()

movie = 'John Wick'
print('my favorite movie is {}.' .format(movie)) #string format method
print('my favorite movie is %s.' %movie) #percent format method
print(f'my favorite movie is {movie}') #f string literal latest way
nl()

#DICTIONARIES - key/value pairs{}