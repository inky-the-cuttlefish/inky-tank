# Platelet gap slider: watch the color shift as the gaps widen.
import time

START = (150, 10, 20)    # deep red (packed platelets)
END = (250, 225, 150)    # pale straw (sparse platelets)
MAX_GAP = 10
SHADES = "@#%*+=-:. "

NAMES = [
    "crimson", "scarlet", "rose", "salmon", "coral",
    "peach", "apricot", "sand", "cream", "straw", "pale gold",
]


def lerp(a, b, t):
    return int(round(a + (b - a) * t))


def color_at(gap):
    t = gap / MAX_GAP
    return tuple(lerp(s, e, t) for s, e in zip(START, END))


def slider(gap):
    bar = ["-"] * (MAX_GAP + 1)
    bar[gap] = "O"
    return "[" + "".join(bar) + "]"


def platelets(gap, count=6):
    cell = "(o)" + " " * gap
    return (cell * count).rstrip()


def shade_bar(gap):
    idx = round(gap * (len(SHADES) - 1) / MAX_GAP)
    return SHADES[idx] * 24


def swatch(r, g, b):
    # ANSI truecolor background block; terminals without support just show spaces
    return "\x1b[48;2;%d;%d;%dm" % (r, g, b) + " " * 24 + "\x1b[0m"


def frame(gap):
    r, g, b = color_at(gap)
    print("gap %2d  %s" % (gap, slider(gap)))
    print("  cells : " + platelets(gap))
    print("  color : %-10s rgb(%3d,%3d,%3d)  #%02X%02X%02X" %
          (NAMES[gap], r, g, b, r, g, b))
    print("  shade : " + shade_bar(gap))
    print("  swatch: " + swatch(r, g, b))
    print()


def main():
    print("=== PLATELET GAP SLIDER ===")
    print("Sliding the gap up, then back down...")
    print()
    sweep = list(range(0, MAX_GAP + 1)) + list(range(MAX_GAP - 1, -1, -1))
    for gap in sweep:
        frame(gap)
        time.sleep(0.15)
    print("Done! Tight packing = deep red, wide gaps = pale straw.")


main()
