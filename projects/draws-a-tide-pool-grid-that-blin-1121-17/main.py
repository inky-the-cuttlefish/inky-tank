import random

random.seed(7)

W, H = 40, 14
FRAMES = 6
PALETTES = [".,:;", "oO0@", "~-=+", "#%&*"]
CREATURES = {(8, 4): "C", (27, 9): "C", (18, 7): "s"}


def in_pool(x, y):
    cx, cy = W / 2, H / 2
    dx = (x - cx) / (W / 2 - 1)
    dy = (y - cy) / (H / 2 - 0.5)
    return dx * dx + dy * dy <= 1.0


def edge(x, y):
    if not in_pool(x, y):
        return False
    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if not in_pool(nx, ny):
            return True
    return False


def base(x, y, t):
    if edge(x, y):
        pal = PALETTES[(t + x // 3) % len(PALETTES)]
        return pal[(x + y + t) % len(pal)]
    pal = PALETTES[(x // 8 + y // 5 + t) % len(PALETTES)]
    if random.random() < 0.15:
        return random.choice(pal)
    return pal[(x * 2 + y + t * 2) % len(pal)]


def cell(x, y, t):
    if not in_pool(x, y):
        return " " if (x + y) % 7 else "^"
    ch = base(x, y, t)
    if (x, y) in CREATURES:
        # Creatures camouflage in the last half of the frames
        if t < FRAMES // 2:
            return CREATURES[(x, y)]
    return ch


def frame(t):
    return "\n".join(
        "".join(cell(x, y, t) for x in range(W)) for y in range(H)
    )


print("TIDE POOL: cuttlefish camouflage in %d frames" % FRAMES)
for t in range(FRAMES):
    print("\n--- frame %d ---" % (t + 1))
    print(frame(t))

print("\nThe cuttlefish (C) vanish into the pattern. Can you find them?")
