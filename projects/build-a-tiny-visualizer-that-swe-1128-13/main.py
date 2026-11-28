import math

WIDTH = 60
ROWS = 7
SHADES = " .:-=+*#%@"


def surface_normal_angle(x, row):
    # Rippled surface: slope varies with position and row
    slope = math.sin(x * 0.45 + row * 0.8) * 0.5
    slope += math.sin(x * 0.17 - row * 0.5) * 0.3
    return slope


def brightness(x, row, light_deg):
    light = math.radians(light_deg)
    normal = surface_normal_angle(x, row)
    # Reflection direction = 2*normal - light; compare to viewer at 0
    reflect = 2 * normal - light
    spec = math.cos(reflect) ** 24
    diffuse = max(0.0, math.cos(normal - light)) * 0.25
    return min(1.0, spec + diffuse)


def render(light_deg):
    lines = []
    for row in range(ROWS):
        chars = []
        for x in range(WIDTH):
            b = brightness(x, row, light_deg)
            idx = int(b * (len(SHADES) - 1))
            chars.append(SHADES[idx])
        lines.append("".join(chars))
    return lines


def main():
    print("=" * WIDTH)
    print("SHIMMER SWEEP: light angle moves, highlights dance")
    print("=" * WIDTH)
    angles = list(range(-60, 61, 20))
    for deg in angles:
        bar_pos = int((deg + 60) / 120 * (WIDTH - 1))
        track = ["-"] * WIDTH
        track[bar_pos] = "O"
        print("light angle: %+4d deg" % deg)
        print("".join(track))
        for line in render(deg):
            print(line)
        print()
    print("Sweep complete. Notice how bright patches slide and shift.")


if __name__ == "__main__":
    main()
