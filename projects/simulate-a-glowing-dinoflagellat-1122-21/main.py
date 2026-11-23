import math
import random

random.seed(7)

W, H = 40, 12
FRAMES = 12
SHADES = " .:*O@"  # dark -> bright

glow = [[0] * W for _ in range(H)]

cells = set()
for _ in range(110):
    cells.add((random.randrange(W), random.randrange(H)))


def stir_position(t):
    """Stirring stick moves in a circle around the tank center."""
    cx, cy = W / 2, H / 2
    ang = t * 0.9
    x = int(cx + math.cos(ang) * (W / 3))
    y = int(cy + math.sin(ang) * (H / 2.6))
    x = max(0, min(W - 1, x))
    y = max(0, min(H - 1, y))
    return x, y


def stir(x, y, radius_sq=9):
    for (cx, cy) in cells:
        dx = (cx - x) / 2.0  # characters are taller than wide
        dy = cy - y
        if dx * dx + dy * dy <= radius_sq:
            glow[cy][cx] = 5


def fade():
    for y in range(H):
        for x in range(W):
            if glow[y][x] > 0:
                glow[y][x] -= 1


def render(sx, sy, stirring):
    border = "+" + "-" * W + "+"
    lines = [border]
    for y in range(H):
        row = ""
        for x in range(W):
            if stirring and (x, y) == (sx, sy):
                row += "/"
            elif (x, y) in cells:
                row += SHADES[glow[y][x]] if glow[y][x] else "."
            else:
                row += " "
        lines.append("|" + row + "|")
    lines.append(border)
    return "\n".join(lines)


print("Bioluminescent tank: calm water, faint specks.")
for t in range(FRAMES):
    stirring = 2 <= t <= 8
    sx, sy = stir_position(t)
    if stirring:
        stir(sx, sy)
    label = "STIRRING! flash!" if stirring else ("calm" if t < 2 else "settling...")
    print()
    print("Frame %d - %s" % (t, label))
    print(render(sx, sy, stirring))
    fade()
print()
print("The water is still again. Glow fades to dark.")
