import random
import time

WIDTH = 50
HEIGHT = 10
FRAMES = 50
RADIUS = 5

random.seed(7)

# Plankton: dict of (x, y) -> glow level (0 = dim)
plankton = {}
while len(plankton) < 45:
    pos = (random.randrange(WIDTH), random.randrange(HEIGHT))
    plankton[pos] = 0

CUTTLE = "<(o_o)>"


def glow_char(level):
    if level >= 3:
        return "@"
    if level == 2:
        return "O"
    if level == 1:
        return "o"
    return "."


def step(frame):
    # Cuttlefish swims left to right, bobbing between two rows
    cx = int(frame * (WIDTH - len(CUTTLE)) / (FRAMES - 1))
    cy = HEIGHT // 2 + (1 if (frame // 6) % 2 == 0 else -1)
    cy = max(0, min(HEIGHT - 1, cy))
    center_x = cx + len(CUTTLE) // 2

    flashes = 0
    for pos in list(plankton):
        x, y = pos
        dist = abs(x - center_x) + abs(y - cy) * 2
        if dist <= RADIUS:
            plankton[pos] = 3
            flashes += 1
        elif plankton[pos] > 0:
            plankton[pos] -= 1

    grid = [[" "] * WIDTH for _ in range(HEIGHT)]
    for (x, y), level in plankton.items():
        grid[y][x] = glow_char(level)
    for i, ch in enumerate(CUTTLE):
        if 0 <= cx + i < WIDTH:
            grid[cy][cx + i] = ch

    border = "+" + "-" * WIDTH + "+"
    lines = [border]
    for row in grid:
        lines.append("|" + "".join(row) + "|")
    lines.append(border)
    lines.append("Frame %02d  Plankton flashing: %d" % (frame + 1, flashes))
    return "\n".join(lines)


def main():
    print("=== Glowing Plankton ===")
    for frame in range(FRAMES):
        print(step(frame))
        print()
        time.sleep(0.1)
    print("The cuttlefish glides on, leaving a trail of fading sparkles.")


if __name__ == "__main__":
    main()
