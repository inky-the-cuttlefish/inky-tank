import random
import math

W, H = 40, 12
N = 14
K = 3
STEPS = 30
FRAMES_EVERY = 6

random.seed(7)

SYMBOLS = [">", "/", "^", "\\", "<", "/", "v", "\\"]


def arrow(angle):
    a = angle % (2 * math.pi)
    idx = int((a + math.pi / 8) / (math.pi / 4)) % 8
    return SYMBOLS[idx]


def wrap_delta(a, b, size):
    d = b - a
    if d > size / 2:
        d -= size
    elif d < -size / 2:
        d += size
    return d


def dist(f, g):
    dx = wrap_delta(f["x"], g["x"], W)
    dy = wrap_delta(f["y"], g["y"], H)
    return math.hypot(dx, dy * 2)


def make_fish():
    return {
        "x": random.uniform(0, W),
        "y": random.uniform(0, H),
        "a": random.uniform(0, 2 * math.pi),
    }


def step(fish):
    new_angles = []
    for f in fish:
        others = sorted((g for g in fish if g is not f), key=lambda g: dist(f, g))
        sx = math.cos(f["a"])
        sy = math.sin(f["a"])
        for g in others[:K]:
            sx += math.cos(g["a"])
            sy += math.sin(g["a"])
        target = math.atan2(sy, sx)
        new_angles.append(target + random.uniform(-0.15, 0.15))
    for f, a in zip(fish, new_angles):
        f["a"] = a
        f["x"] = (f["x"] + math.cos(a)) % W
        f["y"] = (f["y"] - math.sin(a) * 0.5) % H


def order(fish):
    sx = sum(math.cos(f["a"]) for f in fish) / len(fish)
    sy = sum(math.sin(f["a"]) for f in fish) / len(fish)
    return math.hypot(sx, sy)


def render(fish):
    grid = [[" "] * W for _ in range(H)]
    for f in fish:
        grid[int(f["y"]) % H][int(f["x"]) % W] = arrow(f["a"])
    lines = ["+" + "-" * W + "+"]
    lines += ["|" + "".join(row) + "|" for row in grid]
    lines.append("+" + "-" * W + "+")
    return "\n".join(lines)


def main():
    fish = [make_fish() for _ in range(N)]
    for t in range(STEPS + 1):
        if t % FRAMES_EVERY == 0:
            print(f"step {t}  alignment {order(fish):.2f}")
            print(render(fish))
            print()
        step(fish)


main()
