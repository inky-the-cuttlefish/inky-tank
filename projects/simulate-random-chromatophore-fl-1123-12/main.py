import random

SIZE = 10
SYMBOLS = ".:*#@"  # five "colors" from light to dark


def make_grid():
    return [[random.randrange(len(SYMBOLS)) for _ in range(SIZE)]
            for _ in range(SIZE)]


def show(grid, step, label):
    print("--- %s (step %d) ---" % (label, step))
    for row in grid:
        print(" ".join(SYMBOLS[c] for c in row))
    print()


def neighbors(r, c):
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < SIZE and 0 <= nc < SIZE:
            yield nr, nc


def roughness(grid):
    # count neighboring pairs that differ in color
    total = 0
    for r in range(SIZE):
        for c in range(SIZE):
            if c + 1 < SIZE and grid[r][c] != grid[r][c + 1]:
                total += 1
            if r + 1 < SIZE and grid[r][c] != grid[r + 1][c]:
                total += 1
    return total


def is_uniform(grid):
    first = grid[0][0]
    return all(cell == first for row in grid for cell in row)


def main():
    grid = make_grid()
    step = 0
    max_steps = 200000
    show(grid, step, "Chaotic skin")
    next_show = 2000
    while not is_uniform(grid) and step < max_steps:
        r = random.randrange(SIZE)
        c = random.randrange(SIZE)
        nr, nc = random.choice(list(neighbors(r, c)))
        # flip this chromatophore to match a random neighbor
        grid[r][c] = grid[nr][nc]
        step += 1
        if step == next_show:
            show(grid, step, "Blending, roughness=%d" % roughness(grid))
            next_show *= 4
    if is_uniform(grid):
        show(grid, step, "Smooth skin, fully blended")
    else:
        show(grid, step, "Stopped early, roughness=%d" % roughness(grid))


if __name__ == "__main__":
    main()
