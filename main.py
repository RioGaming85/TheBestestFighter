import random
import moves
from player import getMaxHealth, Player

punch = moves.Move('punch', 1, lambda: random.randint(3, 6))
kick = moves.Move('kick', 0.70, lambda: random.randint(5,9))
headbutt = moves.Headbutt(0.25, getMaxHealth)
block = moves.Block(1)
ult = moves.Move('ultimate',2,lambda: random.randint(11, 15))

def process(target, player):
  if player.health <= 0:
    print(f'Player {player.name} has died!\nPlayer {target.name} wins!')
    return None
  move = player.prompt()
  move.run(target, player)

def main():
  moves = [punch, kick, block, headbutt]
  player1 = Player('1', moves)
  player2 = Player('2', moves)

  while True:
    process(player2, player1)
    process(player1, player2)
    if player1.health <= 0 or player2.health <= 0:
      break
main()
