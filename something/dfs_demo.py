from grid import Grid
from dfs import DFS

grid = Grid(16,16)
DFS.mutate(grid, True)

grid.to_svg()
grid.to_png()