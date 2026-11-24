import math

W, H = 61, 31
CHAMBERS = 6
STEPS = 30
GROWTH = 0.19
DTH = 0.11          # radians per step (about 3.3 rad per chamber)
R0 = 1.2


def blank():
    return [[" "] * W for _ in range(H)]


def plot(grid, x, y, ch):
    col = int(round(W / 2 + x * 2))
    row = int(round(H / 2 - y))
    if 0 <= col < W and 0 <= row < H:
        grid[row][col] = ch


def pt(theta, scale=1.0):
    r = R0 * math.exp(GROWTH * theta) * scale
    return r * math.cos(theta), r * math.sin(theta)


def draw_frame(n):
    grid = blank()
    marks = "o*+#@%"
    # septa first, so the shell outline is drawn over them
    for c in range(n):
        theta = (c + 1) * STEPS * DTH
        ox, oy = pt(theta)
        ix, iy = pt(theta - 2 * math.pi)  # same angle, one turn inward
        for k in range(0, 13):
            t = k / 12.0
            plot(grid, ix + (ox - ix) * t, iy + (oy - iy) * t, ".")
    for c in range(n):
        ch = marks[c % len(marks)]
        for s in range(STEPS + 1):
            theta = (c * STEPS + s) * DTH
            x, y = pt(theta)
            plot(grid, x, y, ch)
    return "\n".join("".join(row).rstrip() for row in grid)


def main():
    print("=== Growing a nautilus shell ===")
    for n in range(1, CHAMBERS + 1):
        print()
        print("Frame %d: chamber %d added" % (n, n))
        print(draw_frame(n))
    print()
    print("Each new chamber is bigger than the last. Shell complete!")


main()
