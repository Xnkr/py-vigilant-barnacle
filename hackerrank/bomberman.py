
def bomberMan(n, r, c, grid):
    if n == 0 or n == 1:
        return grid
    else:
        full_grid = [i.replace('.','O') for i in grid]
        if n % 2 == 0:
            return full_grid
        else:
            grid = [['0' if j is '.' else '2' for j in i] for i in grid]
            is_four_n_minus_one = (n + 1) % 4 == 0
            for k in range(2,6):
                to_detonate = set()
                for i in range(r):
                    for j in range(c):
                        if grid[i][j] == '0':
                            grid[i][j] = '3'
                        elif grid[i][j] != '1':
                            grid[i][j] = str(int(grid[i][j]) - 1)
                        else:
                            to_detonate.add((i,j))
                            if i + 1 < r:
                                to_detonate.add((i+1,j))
                            if i - 1 >= 0:
                                to_detonate.add((i-1,j))
                            if j + 1 < c:
                                to_detonate.add((i,j+1))
                            if j - 1 >= 0:
                                to_detonate.add((i,j-1))
                for x,y in to_detonate:
                    grid[x][y] = '0'
                if k == 3 and is_four_n_minus_one:
                    return convert_grid_back(grid)                
                elif k == 5:
                    return convert_grid_back(grid)
        
def convert_grid_back(grid):
    return [''.join(['.' if j is '0' else 'O' for j in i]) for i in grid]

grid3 = ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']
grid5 = ['.......', '...O.O.', '....O..', '..O....', 'OO...OO', 'OO.O...']
bomberMan(3,6,7,grid3)
bomberMan(5,6,7,grid5)
