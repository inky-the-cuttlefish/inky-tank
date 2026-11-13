# Cuttlebone buoyancy simulator (stdlib only, ASCII output)

import random

random.seed(7)

CHAMBERS = 8
DEPTH_ROWS = 12
WATER_DENSITY = 1.0


class Cuttlefish:
    def __init__(self):
        self.gas = [0.5] * CHAMBERS   # 0.0 = all fluid, 1.0 = all gas
        self.depth = 6.0
        self.velocity = 0.0

    def density(self):
        avg_gas = sum(self.gas) / CHAMBERS
        return 1.10 - 0.20 * avg_gas

    def adjust(self, target):
        step = 0.08
        for i in range(CHAMBERS):
            if self.depth > target + 0.3:      # too deep: add gas to rise
                self.gas[i] = min(1.0, self.gas[i] + step * random.random())
            elif self.depth < target - 0.3:    # too shallow: add fluid to sink
                self.gas[i] = max(0.0, self.gas[i] - step * random.random())

    def move(self):
        force = WATER_DENSITY - self.density()   # positive -> rises
        # depth increases downward, so rising reduces depth
        self.velocity = self.velocity * 0.7 - force * 2
        self.depth += self.velocity
        if self.depth < 0.0 or self.depth > DEPTH_ROWS - 1.0:
            self.velocity = 0.0
        self.depth = max(0.0, min(DEPTH_ROWS - 1.0, self.depth))


def chamber_char(g):
    if g > 0.66:
        return "#"
    if g > 0.33:
        return "+"
    return "~"


def draw(fish, target, tick):
    print("Tick %02d  depth=%.1f  target=%d  density=%.3f"
          % (tick, fish.depth, target, fish.density()))
    for row in range(DEPTH_ROWS):
        body = "<(o)>" if row == int(round(fish.depth)) else "     "
        mark = "-" if row == target else "."
        side = mark * 4
        extra = ""
        if row == int(round(fish.depth)):
            extra = " [" + "".join(chamber_char(g) for g in fish.gas) + "]"
        print("|" + side + body + side + "|" + extra)
    print("+" + "=" * 13 + "+")


def main():
    print("CUTTLEBONE BUOYANCY LAB")
    print("Chamber key: # mostly gas, + mixed, ~ mostly fluid")
    print("Row of dashes = target depth\n")
    fish = Cuttlefish()
    targets = [2, 9, 4]
    tick = 0
    for target in targets:
        for _ in range(12):
            fish.adjust(target)
            fish.move()
            tick += 1
            if tick % 4 == 0:
                draw(fish, target, tick)


main()
