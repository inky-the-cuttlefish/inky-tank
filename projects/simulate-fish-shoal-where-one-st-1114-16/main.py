import random

random.seed(7)

W, H = 30, 10
TICKS = 12
SPREAD_CHANCE = 0.55
CALM_AFTER = 3

# Place fish randomly in the grid (about 45% density)
fish = {}
for y in range(H):
    for x in range(W):
        if random.random() < 0.45:
            fish[(x, y)] = {"state": "calm", "timer": 0}

# Startle one fish near the center
cands = sorted(fish, key=lambda p: abs(p[0] - W // 2) + abs(p[1] - H // 2))
start = cands[0]
fish[start]["state"] = "panic"
fish[start]["timer"] = CALM_AFTER


def render(tick):
    print("Tick %d" % tick)
    print("+" + "-" * W + "+")
    for y in range(H):
        row = ""
        for x in range(W):
            f = fish.get((x, y))
            if f is None:
                row += " "
            elif f["state"] == "panic":
                row += "@"
            elif f["state"] == "tired":
                row += "o"
            else:
                row += ">"
        print("|" + row + "|")
    print("+" + "-" * W + "+")
    panic = sum(1 for f in fish.values() if f["state"] == "panic")
    print("Panicking: %d / %d" % (panic, len(fish)))
    print()


def neighbors(x, y):
    for dx in (-2, -1, 0, 1, 2):
        for dy in (-1, 0, 1):
            if (dx, dy) != (0, 0):
                yield (x + dx, y + dy)


for t in range(TICKS):
    render(t)
    newly = []
    for (x, y), f in fish.items():
        if f["state"] == "panic":
            for n in neighbors(x, y):
                nf = fish.get(n)
                if nf and nf["state"] == "calm":
                    if random.random() < SPREAD_CHANCE:
                        newly.append(n)
    # age the panicking fish
    for f in fish.values():
        if f["state"] == "panic":
            f["timer"] -= 1
            if f["timer"] <= 0:
                f["state"] = "tired"
    # newly startled fish panic
    for n in newly:
        if fish[n]["state"] == "calm":
            fish[n]["state"] = "panic"
            fish[n]["timer"] = CALM_AFTER

render(TICKS)
tired = sum(1 for f in fish.values() if f["state"] == "tired")
calm = sum(1 for f in fish.values() if f["state"] == "calm")
print("The ripple passed: %d tired, %d never noticed." % (tired, calm))
