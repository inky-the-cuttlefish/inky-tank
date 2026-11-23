import math
import time

# Shimmer palette: dim to bright
SHADES = " .:-=+*#%@"

ROWS = 8
COLS = 16
BRICK_W = 4          # width of each aragonite "brick"
FRAMES = 40


def brick_phase(row, col):
    """Each brick has its own tiny thickness, which shifts its interference color."""
    return (row * 0.9 + col * 0.37) % (2 * math.pi)


def intensity(row, x, angle):
    # Bricks in alternate layers are offset, like real nacre
    offset = (BRICK_W // 2) if row % 2 else 0
    shifted = x + offset
    brick_index = shifted // BRICK_W
    pos_in_brick = shifted % BRICK_W

    # Mortar lines between bricks stay dark
    if pos_in_brick == 0:
        return 0.05

    thickness = brick_phase(row, brick_index)
    # Thin-film style interference: depends on viewing angle and thickness
    wave = math.sin(thickness * 2 + angle * 3 + row * 0.5)
    glint = math.cos(angle * 2 - brick_index * 0.6) ** 2
    value = 0.5 + 0.5 * wave
    return min(1.0, 0.15 + 0.6 * value + 0.4 * glint * value)


def render(angle):
    lines = []
    width = COLS * BRICK_W // 2
    for row in range(ROWS):
        line = ""
        for x in range(width):
            v = intensity(row, x, angle)
            idx = min(len(SHADES) - 1, int(v * (len(SHADES) - 1)))
            line += SHADES[idx]
        lines.append(line)
    return "\n".join(lines)


def main():
    print("NACRE SHIMMER - tilt the light and watch the bricks glint")
    print("=" * 32)
    time.sleep(0.8)
    for frame in range(FRAMES):
        angle = math.sin(frame / FRAMES * 2 * math.pi) * 1.1
        print("\033[2J\033[H", end="")
        print("NACRE SHIMMER")
        print("=" * 32)
        print(render(angle))
        print()
        print("Light angle: %4d deg" % round(math.degrees(angle)))
        time.sleep(0.12)
    print("Done. Shine on!")


if __name__ == "__main__":
    main()
