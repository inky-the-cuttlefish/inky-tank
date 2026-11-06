import math

W, H = 40, 12
SHADES = " .:-=+*#%@"

def scene(x, y):
    """Return (base_intensity, glare_intensity) for a pixel."""
    base = 0.45 + 0.25 * math.sin(x / 5.0) * math.cos(y / 2.0)
    glare = 0.0
    if y >= H // 2:
        stripe = math.sin(x * 0.9 + (y - H // 2) * 1.7)
        glare = max(0.0, stripe) * 0.6
        cx, cy = W // 2, H * 3 // 4
        if abs(x - cx) + 2 * abs(y - cy) < 8:
            glare = 1.0
    return base, glare

def filtered(x, y, angle_deg):
    base, glare = scene(x, y)
    a = math.radians(angle_deg)
    unpol = base * 0.5
    pol = glare * (math.cos(a) ** 2)
    return min(1.0, unpol + pol)

def render(angle_deg):
    rows = []
    for y in range(H):
        row = ""
        for x in range(W):
            v = filtered(x, y, angle_deg)
            idx = min(len(SHADES) - 1, int(v * (len(SHADES) - 1) + 0.5))
            row += SHADES[idx]
        rows.append("|" + row + "|")
    border = "+" + "-" * W + "+"
    return "\n".join([border] + rows + [border])

def main():
    print("=== POLARIZED SUNGLASSES SIMULATOR ===")
    print("Glare off the lake is polarized horizontally.")
    print("Rotating the filter changes how much glare gets through.")
    for angle in (0, 45, 90):
        t = math.cos(math.radians(angle)) ** 2 * 100
        print()
        print(f"Filter angle: {angle:3d} deg   glare transmission: {t:5.1f}%")
        print(render(angle))
    print()
    print("At 90 deg the glint pattern vanishes: the glare is blocked!")

if __name__ == "__main__":
    main()
