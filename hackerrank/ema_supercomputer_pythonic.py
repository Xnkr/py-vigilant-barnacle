from itertools import repeat, chain, combinations

# naive solution should work here -- itertools and composition for sanity preservation
N, M = [int(x) for x in input().strip().split(' ')]
grid = [[c == 'G' for c in input().strip()] for _ in range(N)]

def all_plusses(i0, j0):
    # edge coordinates of all plusses radiating from this location
    # including the 1-square "plus"
    return chain([[(i0, j0)]],
                 zip(zip(range(i0+1, N), repeat(j0)), \
                     zip(reversed(range(0, i0)), repeat(j0)), \
                     zip(repeat(i0), range(j0+1, M)), \
                     zip(repeat(i0), reversed(range(0, j0)))))

def valid_plusses(i0, j0):
    # yields sets of coordinates each describing a valid
    # plus originating at (i0, j0)
    coords = set()
    for edge in all_plusses(i0, j0):
        if all(grid[i][j] for i, j in edge):
            coords.update(edge)
            yield frozenset(coords)
        else:
            return

# finally generate all possible plusses
poss_plusses = chain.from_iterable(valid_plusses(i, j) for i in range(N) for j in range(M))

# find the non-intersecting pair with the largest area product
# (we only need to remember the largest size)
max_size = -1
for p1, p2 in combinations(poss_plusses, 2):
    if not (p1 & p2):
        max_size = max(max_size, len(p1) * len(p2))
        
print(max_size)

## 2

from itertools import product, chain, izip, repeat, takewhile, tee
    

def allPluses(grid, grid_t):
    return chain.from_iterable(
        (
            set(chain(
                izip(repeat(x), range(y - i, y + i + 1)),
                izip(range(x - i, x + i + 1), repeat(y))
            )) for i, vals in takewhile(
                lambda (i, vals): all(v == 'G' for v in vals),
                enumerate(
                    izip(
                        grid[x][y:],
                        grid[x][y::-1],
                        grid_t[y][x:],
                        grid_t[y][x::-1],
                    )
                )
            )
        )
        for x, y in product(range(len(grid)), range(len(grid[0])))
    )


# Complete the twoPluses function below.
def pluses(grid, n=2):
    grid_t = zip(*grid)
    return max(
        reduce(lambda x, y: x * len(y), pluses, 1)
        for pluses in product(*tee(allPluses(grid, grid_t), n))
        # if not any(l & r for l, r in product(pluses, 2))
        if not pluses[0] & pluses[1]
    )