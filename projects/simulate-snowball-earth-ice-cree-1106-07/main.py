import random

random.seed(42)

ROWS = 12
COLS = 40
EPOCHS = 8

OCEAN = "~"
ICE = "#"
SLUSH = ":"


def make_grid():
    return [[OCEAN for _ in range(COLS)] for _ in range(ROWS)]


def seed_poles(grid):
    # Ice starts at the top and bottom rows (the poles)
    for c in range(COLS):
        grid[0][c] = ICE
        grid[ROWS - 1][c] = ICE


def neighbors(r, c):
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, (c + dc) % COLS
        if 0 <= nr < ROWS:
            yield nr, nc


def lat_bonus(r):
    # Colder near the poles, warmer at the equator
    mid = (ROWS - 1) / 2
    dist = abs(r - mid) / mid
    return dist * 0.3


def step(grid):
    new = [row[:] for row in grid]
    for r in range(ROWS):
        for c in range(COLS):
            cell = grid[r][c]
            icy = sum(1 for nr, nc in neighbors(r, c) if grid[nr][nc] == ICE)
            if cell == OCEAN and icy:
                chance = 0.1 + 0.15 * icy + lat_bonus(r) * 0.5
                if random.random() < chance:
                    new[r][c] = SLUSH
            elif cell == SLUSH:
                if random.random() < 0.6 + lat_bonus(r) * 0.3:
                    new[r][c] = ICE
    return new


def coverage(grid):
    total = ROWS * COLS
    ice = sum(row.count(ICE) for row in grid)
    return 100.0 * ice / total


def show(grid, epoch):
    print("=== Epoch %d | ice cover: %5.1f%% ===" % (epoch, coverage(grid)))
    for row in grid:
        print("".join(row))
    print()


def main():
    grid = make_grid()
    seed_poles(grid)
    show(grid, 0)
    for epoch in range(1, EPOCHS + 1):
        grid = step(grid)
        show(grid, epoch)


if __name__ == "__main__":
    main()
