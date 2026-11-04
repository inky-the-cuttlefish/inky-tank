import math
import time
import sys

WIDTH = 64
HEIGHT = 16
FRAMES = 60

SYMBOLS = "-/|\\"


def angle_at(x, y, t):
    stripe = math.sin((x * 0.35) + (y * 0.5) - t * 0.8)
    shimmer = math.sin(x * 0.9 - y * 0.7 + t * 2.1) * 0.35
    swirl = math.cos((x - WIDTH / 2) * 0.12) * math.sin((y - HEIGHT / 2) * 0.3 + t * 0.5)
    value = stripe + shimmer + swirl
    return ((value + 2.5) / 5.0 * 180.0) % 180.0


def degree_of_polarization(x, y, t):
    return 0.5 + 0.5 * math.sin(x * 0.2 + t * 0.4) * math.cos(y * 0.35 - t * 0.3)


def symbol(angle, strength):
    if strength < 0.25:
        return " "
    if strength < 0.45:
        return "."
    index = int(((angle + 22.5) % 180.0) / 45.0) % 4
    return SYMBOLS[index]


def render(t):
    lines = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            row.append(symbol(angle_at(x, y, t), degree_of_polarization(x, y, t)))
        lines.append("".join(row))
    return "\n".join(lines)


def main():
    print("Inky's polarized light shimmer (what a cuttlefish might see)")
    for f in range(FRAMES):
        t = f * 0.25
        sys.stdout.write(render(t) + "\n")
        sys.stdout.flush()
        time.sleep(0.08)
        if f < FRAMES - 1:
            sys.stdout.write("\033[%dA" % HEIGHT)
    print("Done: stripes = e-vector angle, dots = weak polarization.")


if __name__ == "__main__":
    main()
