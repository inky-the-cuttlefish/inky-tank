import random

W, H = 60, 20
N = 40
STEPS = 60
SHOW = (0, 20, 40, 59)

random.seed(7)


class Bird:
    def __init__(self):
        self.x = random.uniform(0, W)
        self.y = random.uniform(0, H)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)


def limit(vx, vy, m):
    s = (vx * vx + vy * vy) ** 0.5
    if s > m:
        return vx / s * m, vy / s * m
    return vx, vy


def step(birds):
    for b in birds:
        cx = cy = ax = ay = sx = sy = 0.0
        n = 0
        for o in birds:
            if o is b:
                continue
            dx, dy = o.x - b.x, o.y - b.y
            d = (dx * dx + dy * dy) ** 0.5
            if d < 18:
                n += 1
                cx += o.x
                cy += o.y
                ax += o.vx
                ay += o.vy
                if d < 2.5 and d > 0:
                    sx -= dx / d
                    sy -= dy / d
        if n:
            b.vx += (cx / n - b.x) * 0.01
            b.vy += (cy / n - b.y) * 0.01
            b.vx += (ax / n - b.vx) * 0.12
            b.vy += (ay / n - b.vy) * 0.12
            b.vx += sx * 0.15
            b.vy += sy * 0.15
        # gentle pull toward the middle so the flock stays in view
        b.vx += (W / 2 - b.x) * 0.002
        b.vy += (H / 2 - b.y) * 0.004
        b.vx, b.vy = limit(b.vx, b.vy, 1.4)
    for b in birds:
        b.x = (b.x + b.vx) % W
        b.y = (b.y + b.vy) % H


def arrow(b):
    if abs(b.vx) >= abs(b.vy):
        return ">" if b.vx > 0 else "<"
    return "v" if b.vy > 0 else "^"


def draw(birds, t):
    grid = [[" "] * W for _ in range(H)]
    for i, b in enumerate(birds):
        x = min(W - 1, int(b.x))
        y = min(H - 1, int(b.y))
        grid[y][x] = arrow(b)
    print("Step %d" % t)
    print("+" + "-" * W + "+")
    for row in grid:
        print("|" + "".join(row) + "|")
    print("+" + "-" * W + "+")
    print()


def main():
    birds = [Bird() for _ in range(N)]
    for t in range(STEPS):
        if t in SHOW:
            draw(birds, t)
        step(birds)


if __name__ == "__main__":
    main()
