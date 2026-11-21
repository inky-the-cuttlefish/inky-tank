import math

F = 50.0
FOCUS = 2000.0
R = 10.0
PIX = 0.03
N = 41
V0 = 1.0 / (1.0 / F - 1.0 / FOCUS)

W_PTS = [(-1, 1), (-0.5, -1), (0, 0.2), (0.5, -1), (1, 1)]

def seg_dist(px, py, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)

def in_w(u, v):
    return any(seg_dist(u, v, W_PTS[i], W_PTS[i + 1]) < 0.2
               for i in range(len(W_PTS) - 1))

def in_disc(u, v):
    return u * u + v * v <= 1.0

def in_pin(u, v):
    return u * u + v * v <= 0.25 ** 2

def samples(mask):
    pts = []
    for i in range(N):
        for j in range(N):
            u = -1 + 2 * i / (N - 1)
            v = -1 + 2 * j / (N - 1)
            if in_disc(u, v) and mask(u, v):
                pts.append((u * R, v * R))
    return pts

def blur(pts, depth):
    v = 1.0 / (1.0 / F - 1.0 / depth)
    k = abs(1.0 - V0 / v)
    return math.sqrt(sum((x * x + y * y) for x, y in pts) / len(pts)) * k

masks = [("W", samples(in_w)), ("disc", samples(in_disc)),
         ("pinhole", samples(in_pin))]
full = len(masks[1][1])

print("W aperture (x = open):")
for r in range(13):
    v = 1 - r / 6.0
    print("  " + "".join("x" if in_w(-1 + c / 10.0, v) and in_disc(-1 + c / 10.0, v)
                         else "." for c in range(21)))

print()
print("light: " + "  ".join(f"{n}={100*len(p)//full:3d}%" for n, p in masks))

depths = [800, 1000, 1250, 1500, 1750, 2000, 2500, 3000, 4000, 6000, 10000]
print()
print(f"sharp if RMS blur < {PIX} mm")
print("depth_mm " + " ".join(f"{n:>8}" for n, _ in masks))
for d in depths:
    cells = []
    for n, p in masks:
        b = blur(p, d)
        cells.append(f"{b:6.3f}{'*' if b < PIX else ' '} ")
    print(f"{d:8d} " + " ".join(cells))
print("* = sharp")
