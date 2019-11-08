from random import randint
from player import Player
from classes import *
from moves import Ult

ult = Ult('Ultimate', 1, lambda: randint(10, 20), 6)

def process(player1, player2):
  if player1.ultCharge >= 15:
    player1.moves.append(ult)
  else:
    player1.moves = player1.moves
    if player2.ultCharge >= 15:
      player2.moves.append(ult)
    else:
      player2.moves = player2.moves
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
      if randint(0, 1) == 0:
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
    ans = input(str(name) + '\'s class:\n > ').upper()
    if ans not in ['MAGE', 'BRAWLER', 'BARD', 'CLERIC']:
      print('Invalid class choice!')
    else:
      x = 0
      if ans == 'MAGE':
        return Mage()
      elif ans == 'BRAWLER':
        return Brawler()
      elif ans == 'BARD':
        return Bard()
      elif ans == 'CLERIC':
        return Cleric()

def main():
    name1 = input('Player 1 Name:\n > ')
    classPick1 = classSelect(name1)
    name2 = input('Player 2 Name:\n > ')
    classPick2 = classSelect(name2)

    player1 = Player(name1, classPick1)
    player2 = Player(name2, classPick2)

    while True:
        if player1.health <= 0 and player2.health <= 0:
            print(
                f'{player1.name} and {player2.name} have KO\'d each other at the same time!'
            )
            print('It\'s a draw!')
            break
        if player1.health <= 0:
            print(f'{player1.name} has died!\n{player2.name} wins!')
            break
        elif player2.health <= 0:
            print(f'{player2.name} has died!\n{player1.name} wins!')
            break
        process(player1, player2)


if __name__ == "__main__":
    main()
