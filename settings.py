# Dimensions
WIDTH = 612   # Width of game surface
HEIGHT = 612  # Height of game surface
ROWS = 17
SQUARE_SIZE = WIDTH // ROWS
GAP_SIZE = 2  # Gap between squares

# Colors
SURFACE_CLR = (15, 15, 15)
GRID_CLR = (20, 20,20)
SNAKE_CLR = (0, 255, 0)
APPLE_CLR = (255, 0, 0)
HEAD_CLR = (255, 0, 0)
VIRTUAL_SNAKE_CLR = (0, 0, 255)

# Game Settings
FPS = 30  # Frames per second
INITIAL_SNAKE_LENGTH = 2
WAIT_SECONDS_AFTER_WIN = 60
MAX_MOVES_WITHOUT_EATING = ROWS * ROWS * ROWS * 2
SNAKE_MAX_LENGTH = ROWS * ROWS - INITIAL_SNAKE_LENGTH

# Variables used in BFS algorithm
GRID = [[i, j] for i in range(ROWS) for j in range(ROWS)]


def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]],
                 [position[0] - 1, position[1]],
                 [position[0], position[1] + 1],
                 [position[0], position[1] - 1]]
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors


def distance(pos1, pos2):
    x1, x2 = pos1[0], pos2[0]
    y1, y2 = pos1[1], pos2[1]
    return abs(x2 - x1) + abs(y2 - y1)


ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}
