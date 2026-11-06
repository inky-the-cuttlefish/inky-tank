import math

W, H = 40, 12
RAMP = " .:-=+*#%@"


def scene(x, y):
    """Return (brightness, polarization_angle_degrees) for a pixel."""
    brightness = 0.5 + 0.1 * math.sin(x / 5.0) + 0.05 * math.cos(y / 2.0)
    angle = 20.0
    cx, cy = 20, 6
    if ((x - cx) / 9.0) ** 2 + ((y - cy) / 3.0) ** 2 <= 1.0:
        angle = 80.0
        brightness += 0.005
    return brightness, angle


def to_char(v):
    v = max(0.0, min(0.999, v))
    return RAMP[int(v * len(RAMP))]


def render(title, fn):
    print(title)
    print("+" + "-" * W + "+")
    for y in range(H):
        row = "".join(to_char(fn(x, y)) for x in range(W))
        print("|" + row + "|")
    print("+" + "-" * W + "+")
    print()


def brightness_view(x, y):
    # Polarization-blind: only sees brightness
    return scene(x, y)[0]


def polarization_view(x, y):
    # Cuttlefish-style: polarization angle edges plus a faint interior fill
    a = scene(x, y)[1]
    diffs = []
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        b = scene(x + dx, y + dy)[1]
        diffs.append(abs(a - b))
    edge = max(diffs) / 60.0
    interior = (a - 20.0) / 60.0 * 0.3
    return edge + interior


def main():
    print("=== CUTTLEFISH VISION SIMULATOR ===")
    print("A shrimp hides in the sand. Can you see it?")
    print()
    render("[Human-ish brightness view: shrimp is invisible]", brightness_view)
    render("[Cuttlefish polarization view: shrimp glows]", polarization_view)
    print("Same scene, different senses. Dinner is served!")


if __name__ == "__main__":
    main()
