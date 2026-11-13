import math
import sys
import time

WIDTH = 60
HEIGHT = 18
FRAMES = 24

# Characters stand in for interference color bands, thin film to thick film
BANDS = " .:-=+*#%@"


def thickness(x, y, t):
    """Film thickness in arbitrary units (0..1) at a point and time."""
    drain = (y / HEIGHT) * (1.0 - 0.02 * t)
    swirl = 0.18 * math.sin(0.35 * x + 0.9 * t + 2.0 * math.sin(0.25 * y + 0.5 * t))
    swirl += 0.12 * math.cos(0.22 * x - 0.4 * y + 0.7 * t)
    return max(0.0, min(1.0, drain + swirl))


def color_band(h):
    # Interference repeats as thickness grows, so wrap around the palette
    phase = (h * 2.2) % 1.0
    return int(phase * len(BANDS)) % len(BANDS)


def in_bubble(x, y):
    cx, cy = WIDTH / 2, HEIGHT / 2
    dx = (x - cx) / (WIDTH / 2)
    dy = (y - cy) / (HEIGHT / 2)
    return dx * dx + dy * dy <= 1.0


def render(t):
    lines = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if in_bubble(x, y):
                row.append(BANDS[color_band(thickness(x, y, t))])
            else:
                row.append(" ")
        lines.append("".join(row).rstrip())
    return "\n".join(lines)


def main():
    print("=== Soap Bubble Shimmer ===")
    animate = sys.stdout.isatty()
    for frame in range(FRAMES):
        t = frame * 0.5
        if animate:
            print("\033[H\033[J=== Soap Bubble Shimmer ===")
        else:
            print("\n--- frame %d ---" % (frame + 1))
        print(render(t))
        if animate:
            time.sleep(0.12)
    print("\nThe film thins, swirls, and shimmers. Pop!")


if __name__ == "__main__":
    main()
