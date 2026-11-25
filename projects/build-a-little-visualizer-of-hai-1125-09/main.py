import random

WIDTH = 60
HEIGHT = 16
SEED = 7

random.seed(SEED)

grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Little glints of light on the glass
for _ in range(25):
    grid[random.randrange(HEIGHT)][random.randrange(WIDTH)] = "."

SLOPE = {-1: "\\", 0: "|", 1: "/"}

def draw_hair(x, y, length):
    """Draw one wavy hair that drifts down the glass."""
    for _ in range(length):
        if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
            break
        drift = random.choice([-1, 0, 0, 1])
        ch = SLOPE[drift]
        if random.random() < 0.12:
            ch = "~"
        grid[y][x] = ch
        x += drift
        y += 1

for _ in range(9):
    draw_hair(random.randrange(WIDTH),
              random.randrange(0, HEIGHT // 2),
              random.randint(4, HEIGHT))

# A few tiny curly hairs, placed only on empty or glint cells
placed = 0
attempts = 0
while placed < 5 and attempts < 200:
    attempts += 1
    x = random.randrange(0, WIDTH - 3)
    y = random.randrange(0, HEIGHT)
    if all(grid[y][x + i] in " ." for i in range(3)):
        for i, ch in enumerate("~s~"):
            grid[y][x + i] = ch
        placed += 1

border = "+" + "-" * WIDTH + "+"
print(border)
for row in grid:
    print("|" + "".join(row) + "|")
print(border)

moods = [
    "Soft light, smooth glass, a few wandering hairs.",
    "Everything is calm. Even the hairs are relaxing.",
    "Small things, stuck gently, being joyful.",
]
print()
print(random.choice(moods))
