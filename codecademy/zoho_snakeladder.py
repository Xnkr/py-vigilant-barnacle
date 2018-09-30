import random as rnd

board = [i for i in range(0,101)]
snakes = [0]*len(board)
ladder = [0]*len(board)

rnd.seed(0)

for _ in range(15):
	snake_pos = rnd.randint(10,90)
	snake_len = -1 * rnd.randint(1,snake_pos)
	snakes[snake_pos] = snake_len
	ladder_pos  = rnd.randint(5,80)
	ladder_len = rnd.randint(1,len(board)-1-ladder_pos)
	while snakes[ladder_pos] != 0 and snakes[ladder_pos+ladder_len] != 0:
		ladder_pos = rnd.randint(1,80)
		ladder_len = rnd.randint(ladder_pos,len(board)-1)	
	ladder[ladder_pos] = ladder_len

player_pos = 1
moves = 0
traverse = []
dice_rolls = []
ladder_count = snake_count = 0
while(player_pos < len(board)-1):
	moves += 1
	dice_roll = rnd.randint(1,6)
	dice_rolls.append(dice_roll)
	player_pos = board[player_pos] + dice_roll
	if player_pos >= len(board):
		traverse.append(player_pos)
		break
	snake_count += 1 if snakes[player_pos] != 0 else 0
	ladder_count += 1 if ladder[player_pos] != 0 else 0
	player_pos += snakes[player_pos] + ladder[player_pos]
	traverse.append(player_pos)

print "Finished in {0} rolls, {1} climbs and {2} bites".format(moves, ladder_count, snake_count)
print dice_rolls
print traverse