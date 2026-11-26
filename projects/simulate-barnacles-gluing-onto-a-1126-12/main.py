import random

random.seed(7)

WIDTH = 40
ROCK_ROWS = 3
TICKS = 12
STAGES = [
    (0, ".", "liquid goo"),
    (3, "o", "curing"),
    (6, "O", "firm"),
    (10, "A", "rock solid"),
]


class Barnacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hardness = 0.0

    def update(self):
        # tide splashes give the cement a random curing boost
        self.hardness += 1.0 + random.random() * 0.5

    def _stage(self):
        current = STAGES[0]
        for stage in STAGES:
            if self.hardness >= stage[0]:
                current = stage
        return current

    def symbol(self):
        return self._stage()[1]

    def stage_name(self):
        return self._stage()[2]


def draw(barnacles, tick):
    grid = [[" " for _ in range(WIDTH)] for _ in range(ROCK_ROWS)]
    for b in barnacles:
        grid[b.y][b.x] = b.symbol()
    print("Tide cycle %2d  (%d barnacles)" % (tick, len(barnacles)))
    print("~" * WIDTH)
    for row in grid:
        print("".join(row))
    print("#" * WIDTH)
    print()


def main():
    barnacles = []
    taken = set()
    for tick in range(1, TICKS + 1):
        for _ in range(random.randint(1, 3)):
            x = random.randrange(WIDTH)
            y = random.randrange(ROCK_ROWS)
            if (x, y) not in taken:
                taken.add((x, y))
                barnacles.append(Barnacle(x, y))
        for b in barnacles:
            b.update()
        if tick % 3 == 0:
            draw(barnacles, tick)
    counts = {}
    for b in barnacles:
        counts[b.stage_name()] = counts.get(b.stage_name(), 0) + 1
    print("Final cement report:")
    for _, _, label in STAGES:
        print("  %-12s %d" % (label, counts.get(label, 0)))


main()
