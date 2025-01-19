import random
from make_animation import MakeAnimation

class DFS:

    def mutate(grid, animation = False, cell_size=20, fps=10):
        start = current = grid.random_cell()
        stack = [start]
        filenames = []
        index = 0

        while stack:
            current = stack[-1]
            unvisited_neighbors = [cell for cell in current.neighbors() if len(cell.get_links()) == 0]

            if unvisited_neighbors:
                neighbor = random.choice(unvisited_neighbors)
                current.link(neighbor)
                stack.append(neighbor)
                index += 1
                if animation:
                    grid.distances = start.distances()
                    grid.maximum = grid.distances.max()[1]
                    grid.to_png(cell_size, str(index))
                    filenames.append("./exports/maze"+str(index)+".png")
            else:
                stack.pop()

        if animation:
            MakeAnimation(filenames, 'dfs.gif', fps)