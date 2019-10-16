from random import randint
import moves
from player import Player

punch = moves.Move('punch', 1, lambda: randint(3, 6), 3)
kick = moves.Move('kick', 0.70, lambda: randint(7, 10), 2)
headbutt = moves.Headbutt(0.25, randint(15, 20), 1)
block = moves.Block(1, 5)
ult = moves.Ult(1, lambda: randint(12,17), 4)

def process(player1, player2):
  if player1.ultCharge >= 5:
    player1.moves = [punch, kick, block, headbutt, ult]
  else:
    player1.moves = [punch, kick, block, headbutt]
  if player2.ultCharge >= 5:
    player2.moves = [punch, kick, block, headbutt, ult]
  else:
    player2.moves = [punch, kick, block, headbutt]
  move1 = player1.prompt()
  move2 = player2.prompt()

  print('\n-------------------------------------------')
  if move1.getSpeed > move2.getSpeed:
      print(f'Player {player1.name} moves first!')
      move1.run(player2, player1)
      move2.run(player1, player2)
  elif move2.getSpeed > move1.getSpeed:
      print(f'Player {player2.name} moves first!')
      move2.run(player1, player2)
      move1.run(player2, player1)
  else:
      if randint(0, 1) == 0:
          print(f'Player {player1.name} moves first!')
          move1.run(player2, player1)
          move2.run(player1, player2)
      else:
          print(f'Player {player2.name} moves first!')
          move2.run(player1, player2)
          move1.run(player2, player1)
  print('-------------------------------------------')


def main():
    moves = [punch, kick, block, headbutt]
    player1 = Player('1', moves)
    player2 = Player('2', moves)

    while True:
        if player1.health <= 0 and player2.health <= 0:
          print(f'Player {player1.name} and Player {player2.name} have KO\'d each other at the same time!')
          print('It\'s a draw!')
          break
        if player1.health <= 0:
          print(f'Player {player1.name} has died!\nPlayer {player2.name} wins!')
          break
        elif player2.health <= 0:
          print(f'Player {player2.name} has died!\nPlayer {player1.name} wins!')
          break
        process(player1, player2)


if __name__ == "__main__":
    main()
