from random import randint, choice
from player import Player, displayMenu
from cpuPlayer import cpuPlayer
from moves import Ult
from classes import *

ult = Ult('Ultimate', 1, lambda: randint(10, 20), 6)

def ultChargeProc(player):
  if len(player.moves) > 4 and player.ultCharge < 15:
    player.moves[len(player.moves)-1].remove()
  elif player.ultCharge >= 15 and len(player.moves) < 5:
    player.moves.append(ult)
  elif len(player.moves) == 4 and player.ultCharge < 15:
      pass
  else:
    pass  
def process(player1, player2):

  ultChargeProc(player1)
  ultChargeProc(player2)
  move1 = player1.prompt()
  move2 = player2.prompt()

  print('\n-------------------------------------------')
  if move1.getSpeed > move2.getSpeed:
    print(f'{player1.name} moves first!')
    move1.run(player2, player1)
    move2.run(player1, player2)
  elif move2.getSpeed > move1.getSpeed:
    print(f'{player2.name} moves first!')
    move2.run(player1, player2)
    move1.run(player2, player1)
  else:
    if randint(0, 1) == 0: # if moves have the same speed
      print(f'{player1.name} moves first!')
      move1.run(player2, player1)
      move2.run(player1, player2)
    else:
      print(f'{player2.name} moves first!')
      move2.run(player1, player2)
      move1.run(player2, player1)
  print('-------------------------------------------')

def classSelect(name):
  ans = ''
  x = 1
  while x != 0:
    classArray = ['MAGE', 'MONK', 'BARD', 'CLERIC']
    print(f'{str(name)}\'s class:')
    ans = displayMenu(classArray)
    classInpArr = []
    for j in range(len(classArray)):
      classInpArr.append(str(j))
    if ans not in classInpArr:
      print('Invalid class choice!')
    else:
      x = 0
      ans = int(ans)
      if ans == 0:
        return Mage()
      elif ans == 1:
        return Monk()
      elif ans == 2:
        return Bard()
      elif ans == 3:
        return Cleric()
      elif ans == 4:
        return Goose()

def singlePlayer():
  if randint(0,9) < 9: # 2% chance of AI being a Goose
    aiClasses = [Mage(), Monk(), Bard(), Cleric()]
  else:
    aiClasses = [Mage(), Monk(), Bard(), Cleric(), Goose()]
  pname = input('Player Name:\n > ')
  classPick = classSelect(pname)
  player = Player(pname, classPick)
  cpu = cpuPlayer('CPU', choice(aiClasses))
  while True:
    if player.health <= 0 and cpu.health <= 0:
      print(f'{player.name} and {cpu.name} have KO\'d each other at the same time!')
      print('It\'s a draw!')
      break
    if player.health <= 0:
      print(f'{player.name} has died!\n{cpu.name} wins!')
      break
    elif cpu.health <= 0:
      print(f'{cpu.name} has died!\n{player.name} wins!')
      break
    process(player, cpu)

def twoPlayer():
  name1 = input('Player 1 Name:\n > ')
  classPick1 = classSelect(name1)
  name2 = input('Player 2 Name:\n > ')
  classPick2 = classSelect(name2)
  player1 = Player(name1, classPick1)
  player2 = Player(name2, classPick2)

  while True:
    if player1.health <= 0 and player2.health <= 0:
      print(f'{player1.name} and {player2.name} have KO\'d each other at the same time!')
      print('It\'s a draw!')
      break
    if player1.health <= 0:
      print(f'{player1.name} has died!\n{player2.name} wins!')
      break
    elif player2.health <= 0:
      print(f'{player2.name} has died!\n{player1.name} wins!')
      break
    process(player1, player2)

def main():
  ans = ''
  x = False
  while x != True:
    ans = displayMenu(['Single Player', 'Two Player'])
    if ans == '0':
      x = True
      singlePlayer()
    elif ans == '1':
      x = True
      twoPlayer()
    else:
      print('Invalid Input')


main()
