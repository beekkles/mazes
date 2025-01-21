from grid import Grid
from hilbert import Hilbert
from dfs import DFS

grid = Grid(16,16)
Hilbert.mutate(grid, animation=False)
#DFS.mutate(grid, False)

grid.to_svg()
grid.to_png()