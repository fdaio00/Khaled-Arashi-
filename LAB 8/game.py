from random import *

game_list = ['rock' , 'paper', 'scissor']
print(game_list)

uc = input('Enter Your Choice : ')


def userChoice():
    if uc in game_list:
        return uc
    else:
        return 0
    
def computerChoice():
    cc = randint(0,2)
    return game_list[cc]

def winnerChoice(user , computer):
    if user==computer:
        print('Try Again')
    elif (
        (user=='rock' and computer=='scissor') or
        (user=='scissor' and computer=='paper') or
        (user=='paper' and computer=='rock')
          ):
        print('You Won....')
    elif userChoice()==0:
        print('You entered worng item.')
    else:
        print('Computer Won....')


cc = computerChoice()
print('---------------------')
print('Your Choice : ',uc)
print('Computer Choice : ',cc)
print('---------------------')
winnerChoice(uc , cc)
print('---------------------')