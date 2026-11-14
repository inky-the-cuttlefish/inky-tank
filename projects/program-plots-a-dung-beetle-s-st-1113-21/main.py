import math
import random

random.seed(42)

W, H = 60, 22
grid = [[" " for _ in range(W)] for _ in range(H)]

target = (46.0, 2.0)

# Milky Way: diagonal band through the target, bottom-left to top-right
for y in range(H):
    for x in range(W):
        d = abs((x - target[0]) + (y - target[1]) * 1.6) / 1.9
        if d < 5 and random.random() < 0.6 - d * 0.1:
            grid[y][x] = random.choice([".", "*", "+"])

# Scattered background stars
for _ in range(25):
    x = random.randrange(W)
    y = random.randrange(H)
    if grid[y][x] == " ":
        grid[y][x] = "."

# Beetle path
x, y = 3.0, float(H - 2)
start = (int(x), int(y))
heading = math.atan2(target[1] - y, target[0] - x)
steps = 0
arrived = False
CLOUD = range(18, 29)

while steps < 300:
    steps += 1
    cloudy = steps in CLOUD
    want = math.atan2((target[1] - y) / 0.7, (target[0] - x) / 1.3)
    if cloudy:
        heading += random.uniform(-0.8, 0.8)
    else:
        heading += random.uniform(-0.1, 0.1)
        diff = math.atan2(math.sin(want - heading), math.cos(want - heading))
        heading += diff * 0.2
    x += math.cos(heading) * 1.3
    y += math.sin(heading) * 0.7
    ix, iy = int(round(x)), int(round(y))
    if not (0 <= ix < W and 0 <= iy < H):
        break
    if cloudy:
        grid[iy][ix] = "?"
    elif grid[iy][ix] in (" ", ".", "*", "+"):
        grid[iy][ix] = "o"
    if math.hypot(target[0] - x, target[1] - y) < 2.0:
        arrived = True
        break

grid[start[1]][start[0]] = "S"

print("=" * W)
print("DUNG BEETLE STAR COMPASS".center(W))
print("=" * W)
for row in grid:
    print("".join(row))
print("=" * W)
print("S start   o rolling ball   ? clouds hide the stars   */+/. Milky Way")
if arrived:
    print(f"The beetle reached the Milky Way in {steps} steps!")
else:
    print(f"The beetle wandered off after {steps} steps.")
