from random import randrange

def get_row(sudoku, i):
	if i>=0 and i<9:
		return sudoku[i]
	else:
		raise RuntimeError("Not a valid row")

def get_col(sudoku, j):
	if j>=0 and j<9:
		return [sudoku[row][j] for row in range(len(sudoku))]	
	else:
		raise RuntimeError("Not a valid column")

def get_box(sudoku,n):
	if n < 3:
		rows = range(3)
	elif n < 6:
		rows = range(3,6)
	else:
		rows = range(6,9)
	
	if n%3 == 0:
		cols = range(3)
	elif n%3 == 1:
		cols = range(3,6)
	else:
		cols = range(6,9)

	return [sudoku[col][row] for col in cols for row in rows ]

def print_sudo(sudoku):
	s_str = ""
	for row in sudoku:
		s_str += str(row)
		s_str += '\n'
	return s_str

sudo_st = [[1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9],
		  [1,2,3,4,5,6,7,8,9]]
sudo_raw = "003020600 900305001 001806400 008102900 700000008 006708200 002609500 800203009 005010300"
sudo_st = [list(_) for _ in sudo_raw.split(' ')]
fix_idx = [[1 if y!='0' else 0 for y in x]for x in sudo_st]
best_so_far = [[sudo_st[i][j] if fix_idx[i][j] == 1 else randrange(1,10) for j in range(len(sudo_st))] for i in range(len(sudo_st))]
def gen_grid(best_so_far,fix_idx):
	pass

print print_sudo(sudo_st)
print get_box(sudo_st,8)