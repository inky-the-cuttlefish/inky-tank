import random

random.seed(7)

WIDTH = 40
HEIGHT = 8
LAYERS_TO_SET = 4  # protein layers needed before a barnacle is fully glued
STAGES = [0, 5, 15, 30]  # ticks at which to print the hull

PROTEINS = ["primer", "lipid film", "amyloid glue", "cross-linked cement"]
SYMBOLS = [".", ":", "o", "A"]  # index = layers - 1


class Barnacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.layers = 1

    def secrete(self):
        if self.layers < LAYERS_TO_SET:
            self.layers += 1

    @property
    def glued(self):
        return self.layers >= LAYERS_TO_SET

    def symbol(self):
        # grows from a speck into a full cone as layers build up
        return SYMBOLS[min(self.layers, LAYERS_TO_SET) - 1]


def draw(hull, tick):
    print("--- tick %d ---" % tick)
    print("~" * WIDTH)
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            b = hull.get((x, y))
            row.append(b.symbol() if b else "=")
        print("".join(row))
    print("~" * WIDTH)
    total = len(hull)
    done = sum(1 for b in hull.values() if b.glued)
    print("barnacles: %d  fully glued: %d" % (total, done))
    print()


def main():
    hull = {}
    print("SHIP HULL BIOFOULING SIMULATOR")
    print("Layers: " + " -> ".join(PROTEINS))
    print()
    for tick in range(0, 31):
        # existing barnacles add a protein layer
        for b in hull.values():
            b.secrete()
        # new larvae land on bare spots
        for _ in range(3):
            x = random.randrange(WIDTH)
            y = random.randrange(HEIGHT)
            if (x, y) not in hull:
                hull[(x, y)] = Barnacle(x, y)
        if tick in STAGES:
            draw(hull, tick)
    print("The hull is fouled. Time for the scrub brushes!")


main()
