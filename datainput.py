import mysql.connector

# connect to db
mydb = mysql.connector.connect(
    host = 'host',
    user = 'user',
    password = 'password'
)

class pet:
    def __init__(self):
        self.name = ''
        self.level = 0
        self.hp = 0
        self.attack = 0
        self.perk = ''
        self.trumpets = 0
        self.mana = 0


print('Input data in the format of "P1,P2,P3,P4,P5" (i.e. 3,7,9,13,19). If you do not have a pet in that position, or the pet does not have the specified quality, input "0" or "None" for the value.')
# name = input (figure out names later)

def inputcheck(userinput, datatype):
    formatted = [i.strip() for i in userinput.split(',')]
    if datatype == int: # typecast list elements to int
        formatted = list(map(int, formatted))
    if all(isinstance(i, datatype) for i in formatted) == True: # check if all elements match datatype
        print(formatted)
        return formatted
    else:
        return False

levels = False
while levels == False:
    levels = input('What level is each pet?: ')
    levels = inputcheck(levels, int)

hp = False
while hp == False:
    hp = input('How much health does each pet have?: ')
    hp = inputcheck(hp, int)

atk = False
while atk == False:
    atk = input('How much attack does each pet have?: ')
    atk = inputcheck(atk, int)

trumpets = False
while trumpets == False:
    trumpets = input('How many trumpets does each pet have?: ')
    trumpets = inputcheck(trumpets, int)

mana = False
while mana == False:
    mana = input('How much mana does each pet have?: ')
    mana = inputcheck(mana, int)





# define helper function
# def check(list, datatype)
#    if all elements in list match datatype: return true, otherwise return false

# user should input comma separated integers
# use .split() to split values into list
# how to check for integers?

# do easy soln first before improving


