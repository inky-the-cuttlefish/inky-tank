import math
import random

random.seed(7)

SHADES = " .:-=+*#%@"
WIDTH = 40
HEIGHT = 8
FRAMES = 6


def wavelength_for(spacing):
    # Thin-film style: reflected wavelength roughly proportional to spacing.
    return spacing * 2.0


def color_name(wl):
    if wl < 450:
        return "violet"
    if wl < 495:
        return "blue"
    if wl < 570:
        return "green"
    if wl < 590:
        return "yellow"
    if wl < 620:
        return "orange"
    return "red"


def make_cells():
    # Small random jitter so the skin ripples but is not pure noise.
    return [[random.uniform(-0.6, 0.6) for _ in range(WIDTH)]
            for _ in range(HEIGHT)]


def spacing_at(x, y, jitter, t):
    # Platelet spacing in nm, oscillating like tuning iridophores.
    wave = math.sin(t * 0.9 + jitter + x * 0.15 + y * 0.3)
    return 250 + 80 * wave  # 170..330 nm -> 340..660 nm reflected


def render(cells, t):
    lines = []
    counts = {}
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            sp = spacing_at(x, y, cells[y][x], t)
            wl = wavelength_for(sp)
            name = color_name(wl)
            counts[name] = counts.get(name, 0) + 1
            idx = int((wl - 340) / (660 - 340) * (len(SHADES) - 1))
            idx = max(0, min(len(SHADES) - 1, idx))
            line += SHADES[idx]
        lines.append(line)
    return lines, counts


def main():
    cells = make_cells()
    print("=== Tiny Squid Skin Simulator ===")
    print("Light = short wavelength (violet), dense = long (red)")
    for f in range(FRAMES):
        t = f * 1.0
        lines, counts = render(cells, t)
        print()
        print("Frame %d (t=%.1f)" % (f + 1, t))
        print("+" + "-" * WIDTH + "+")
        for line in lines:
            print("|" + line + "|")
        print("+" + "-" * WIDTH + "+")
        total = WIDTH * HEIGHT
        dominant = max(counts, key=counts.get)
        summary = ", ".join("%s %d%%" % (n, 100 * c // total)
                            for n, c in sorted(counts.items(),
                                               key=lambda kv: -kv[1]))
        print("Dominant: %s | %s" % (dominant, summary))


if __name__ == "__main__":
    main()
