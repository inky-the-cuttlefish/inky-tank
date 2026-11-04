import math
import random

random.seed(7)

# Brightness ramp from dark to brilliant (ASCII only)
RAMP = " .:-=+*#%@"

WIDTH = 48
TICKS = 26           # 0.5h steps, covering about one tidal cycle
STEP = 0.5           # hours per tick
TIDE_PERIOD = 12.4   # hours, roughly high-to-high

# Each bacterium has its own small phase offset and sensitivity
bacteria = [
    {"phase": random.uniform(-0.6, 0.6), "gain": random.uniform(0.7, 1.0)}
    for _ in range(WIDTH)
]


def tide_level(hour):
    """Tide height from 0 (low) to 1 (high)."""
    return 0.5 + 0.5 * math.sin(2 * math.pi * hour / TIDE_PERIOD)


def glow(b, hour):
    """Glow follows the tide, with a bit of flicker."""
    level = 0.5 + 0.5 * math.sin(2 * math.pi * hour / TIDE_PERIOD + b["phase"])
    flicker = random.uniform(-0.08, 0.08)
    value = level * b["gain"] + flicker
    return max(0.0, min(1.0, value))


def render_row(hour):
    chars = []
    for b in bacteria:
        g = glow(b, hour)
        idx = int(g * (len(RAMP) - 1))
        chars.append(RAMP[idx])
    return "".join(chars)


def tide_bar(hour):
    n = int(tide_level(hour) * 20)
    return "[" + "~" * n + " " * (20 - n) + "]"


def main():
    print("=== Squid Light Organ: Bacterial Glow vs. Tide ===")
    print("Dark ' ' -> bright '@'. Tide bar on the right.\n")
    print("hour | organ" + " " * (WIDTH - 5) + " | tide")
    print("-" * (WIDTH + 32))
    for t in range(TICKS):
        hour = t * STEP
        print("%4.1f | %s | %s" % (hour, render_row(hour), tide_bar(hour)))
    print("-" * (WIDTH + 32))
    print("The organ brightens as the tide rises and dims as it falls.")


if __name__ == "__main__":
    main()
