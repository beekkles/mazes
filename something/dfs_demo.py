from grid import Grid
from dfs import DFS

grid = Grid(32,32)
DFS.mutate(grid, True)

grid.to_svg()
grid.to_png()