import math

GROWTH = 1.18       # radius multiplier per chamber
TURN = 0.55         # radians turned per chamber
START_RADIUS = 1.0
CHAMBERS = 24
W, H = 61, 31


def build_shell(n):
    chambers = []
    r = START_RADIUS
    theta = 0.0
    for i in range(1, n + 1):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        chambers.append((i, r, theta, x, y))
        r *= GROWTH
        theta += TURN
    return chambers


def plot(chambers):
    grid = [[" "] * W for _ in range(H)]
    max_r = max(c[1] for c in chambers)
    sx = (W // 2 - 2) / max_r
    sy = (H // 2 - 1) / max_r
    cx, cy = W // 2, H // 2
    # draw the spiral curve lightly between chambers
    for k in range(len(chambers) - 1):
        _, r1, t1, _, _ = chambers[k]
        for s in range(12):
            f = s / 12.0
            r = r1 * (GROWTH ** f)
            t = t1 + TURN * f
            px = int(round(cx + r * math.cos(t) * sx))
            py = int(round(cy - r * math.sin(t) * sy))
            if 0 <= px < W and 0 <= py < H:
                grid[py][px] = "."
    # mark each chamber with its last digit
    for i, r, t, x, y in chambers:
        px = int(round(cx + x * sx))
        py = int(round(cy - y * sy))
        if 0 <= px < W and 0 <= py < H:
            grid[py][px] = str(i % 10)
    grid[cy][cx] = "@"
    return "\n".join("".join(row).rstrip() for row in grid)


def main():
    shell = build_shell(CHAMBERS)
    print("=== Tiny Nautilus Shell Growth ===")
    print("Step  Radius   Angle(deg)  Size")
    for i, r, t, x, y in shell:
        bar = "#" * max(1, int(r))
        print(f"{i:4d} {r:7.2f} {math.degrees(t):10.1f}    {bar}")
    print(f"\nShell finished with {len(shell)} chambers.")
    print("Spiral map (digit = chamber number mod 10, @ = center):\n")
    print(plot(shell))


if __name__ == "__main__":
    main()
