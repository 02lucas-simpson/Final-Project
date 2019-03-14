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
"""
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

"""



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