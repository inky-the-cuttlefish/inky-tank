import random
import math

random.seed(7)

WIDTH = 40
HEIGHT = 12
NUM_FLAKES = 28

TILTS = ["-", "/", "|", "\\"]
SHADES = [".", ":", "o", "O", "@"]
COLORS = [31, 33, 32, 36, 34, 35]


class Flake:
    def __init__(self):
        self.x = random.uniform(1, WIDTH - 2)
        self.y = random.uniform(1, HEIGHT - 2)
        self.angle = random.uniform(0, math.pi)
        self.hue = random.uniform(0, 1)

    def clamp(self):
        self.x = min(max(self.x, 1), WIDTH - 2)
        self.y = min(max(self.y, 1), HEIGHT - 2)

    def wiggle(self, force):
        self.x += random.uniform(-1, 1) * force
        self.y += random.uniform(-0.6, 0.6) * force
        self.angle += random.uniform(-1, 1) * force * 0.8
        self.hue = (self.hue + random.uniform(0.0, 0.25) * force) % 1.0
        self.clamp()

    def settle(self):
        self.y += random.uniform(-0.15, 0.15)
        self.x += random.uniform(-0.2, 0.2)
        self.angle *= 0.7
        self.clamp()

    def glyph(self):
        a = self.angle % math.pi
        return TILTS[int((a / math.pi) * len(TILTS)) % len(TILTS)]

    def color(self):
        return COLORS[int(self.hue * len(COLORS)) % len(COLORS)]


def render(flakes, label, use_color=True):
    grid = [[" "] * WIDTH for _ in range(HEIGHT)]
    for f in flakes:
        grid[int(f.y)][int(f.x)] = (f.glyph(), f.color())
    print("Frame:", label)
    print("+" + "-" * WIDTH + "+")
    for row in grid:
        out = ""
        for c in row:
            if c == " ":
                out += " "
            elif use_color:
                out += "\033[%dm%s\033[0m" % (c[1], c[0])
            else:
                out += c[0]
        print("|" + out + "|")
    print("+" + "-" * WIDTH + "+")


def main():
    flakes = [Flake() for _ in range(NUM_FLAKES)]
    print("TINY PLATELET TANK")
    print("Glyphs / - \\ | show tilt; color shows hue.")
    render(flakes, "calm")
    for step, force in enumerate([1.5, 1.0, 0.0, 0.0], 1):
        for f in flakes:
            if force:
                f.wiggle(force)
            else:
                f.settle()
        render(flakes, "wiggle %d (force %.1f)" % (step, force)
               if force else "settling %d" % step)


if __name__ == "__main__":
    main()
