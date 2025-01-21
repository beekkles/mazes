from make_animation import MakeAnimation

def hilbert_curve(x0, y0, xi, xj, yi, yj, n, result):
    if n <= 0:
        x = x0 + (xi + yi) // 2
        y = y0 + (xj + yj) // 2
        result.append((x, y))
    else:
        hilbert_curve(x0, y0, yi // 2, yj // 2, xi // 2, xj // 2, n - 1, result)
        hilbert_curve(x0 + xi // 2, y0 + xj // 2, xi // 2, xj // 2, yi // 2, yj // 2, n - 1, result)
        hilbert_curve(x0 + xi // 2 + yi // 2, y0 + xj // 2 + yj // 2, xi // 2, xj // 2, yi // 2, yj // 2, n - 1, result)
        hilbert_curve(x0 + xi // 2 + yi, y0 + xj // 2 + yj, -yi // 2, -yj // 2, -xi // 2, -xj // 2, n - 1, result)

def generate_hilbert_path(order):
    result = []
    hilbert_curve(0, 0, 1 << order, 0, 0, 1 << order, order, result)
    return result

class Hilbert:
    @staticmethod
    def mutate(grid, animation=False, cell_size=20, fps=10):
        filenames = []
        index = 0

        order = 1
        while (1 << order) < max(grid.rows, grid.columns):
            order += 1

        hilbert_path = generate_hilbert_path(order)
        current = grid.grid[0][0]

        for x, y in hilbert_path:
            if 0 <= x < grid.columns and 0 <= y < grid.rows:
                cell = grid.grid[x][y]
                if cell:
                    current.link(cell)
                    current = cell
                    
                    if animation:
                        index += 1
                        grid.to_png(cell_size, str(index))
                        filenames.append("./exports/maze"+str(index)+".png")

        if animation:
            MakeAnimation(filenames, 'hilbert.gif', fps=10)