'''
Creator: Lucas Simpson
Resources: Ethan Blow, Stack Overflow, and Google
'''

#added a nice greating

for i in range(50):
    print ("i have to do this to get a good grade")

name = input("What is your name: ")

def greeting():
    print ("Hi there " + name + "!")
    print ("Nice to meet you!")

greeting()


# Declared all variables

adjective = input('Choose an adjective: ')
adjective2 = input('Choose an adjective: ')
noun = input('Choose a noun: ')
noun2 = input('Choose a noun: ')
plural_noun = input('Choose a plural noun: ')
game = input('Choose a game: ')
plural_noun2 = input('Choose a plural noun: ')
verb = input('Choose a verb ending in "ing": ')
verb2 = input('Choose a verb ending in "ing": ')
plural_noun3 = input('Choose a plural noun: ')
verb3 = input('Choose a verb ending in "ing": ')
noun3 = input('Choose a noun: ')
plant = input('Choose a plant: ')
body_part = input('choose a part of the body: ')
place = input('Choose a place: ')
verb4 = input('Choose a verb ending in "ing": ')
adjective3 = input('Choose an adjective: ')
number = input('Choose a number: ')
plural_noun4 = input('Choose a plural noun: ')
print('')
print('')
print('A vacation is when you take a trip to some ' + adjective )
print('place with your ' + adjective2)
print('family. Usually you go some place that is near a/an ' + noun)
print('or up on a/an ' + noun2 )
print('. A good vacation place is one where youcan ride ' +plural_noun)
print('or play ' + game)
print('or go huntiing for ' + plural_noun2)
print('or play ' + verb)
print('or ' +verb2 + '.')
print('When parents go on vacation, they spend their time eating three ' + plural_noun3)
print('a day ' + plural_noun4)
print('and fathers play golf, and mothers sit around ' + verb3 + '. ')
print('Last summer, my litthe brother fell in a/an ' + noun3)   
print('and got poison ' + plant)
print('all over his' + body_part)
print('. My family is goint to (the) ' + place  )
print(', and i will practice ' + verb4 + '. ' )      
print('Parents need vacations more then kids because parents are always very ' + verb3)
print('and because theybhave to work ' + number )
print('hours every day allyear making enough ' + plural_noun5 )
print('to pay for the vacation ')
print('')
print('')
like = -5
while like <1 or like >3:
    try:
        like = float(input('Did you like the madlibs???(1 = yes 2 = No) '))

    except ValueError:
        print('1 or 2')   

if like == 1:
    print('Thank you')

if like == 2:
    print('well ok then i see how it is')
