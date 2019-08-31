def moveQueen(pos_of_queen, n, obstacles, move):
    current_pos = [pos_of_queen[0] + move[0], pos_of_queen[1] + move[1]]
    if current_pos[0] > 0 and current_pos[1] > 0 and current_pos[0] <= n and current_pos[1] <= n:
        if current_pos not in obstacles:
            return 1 + moveQueen(current_pos, n, obstacles, move)
    return 0


def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [-1,0,1]
    moves = list(product(directions,repeat=2))
    moves.remove((0,0))
    moves_of_queen = 0
    for move in moves:
        # moves_of_queen += moveQueen([r_q, c_q], n, obstacles, move)
        current_pos = [r_q, c_q]
        while True:
            current_pos = [current_pos[0] + move[0], current_pos[1] + move[1]]
            if current_pos[0] > 0 and current_pos[1] > 0 and current_pos[0] <= n and current_pos[1] <= n and current_pos not in obstacles:
                moves_of_queen += 1
            else: 
                break
    return moves_of_queen

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    directions = [-1,0,1]
    moves = list(product(directions,repeat=2))
    moves.remove((0,0))
    moves_of_queen = 0
    obstacles = set(tuple(row) for row in obstacles)
    for move in moves:
        # moves_of_queen += moveQueen([r_q, c_q], n, obstacles, move)
        current_pos = (r_q, c_q)
        while True:
            current_pos = (current_pos[0] + move[0], current_pos[1] + move[1])
            if current_pos[0] > 0 and current_pos[1] > 0 and current_pos[0] <= n and current_pos[1] <= n and current_pos not in obstacles:
                moves_of_queen += 1
            else: 
                break
    return moves_of_queen