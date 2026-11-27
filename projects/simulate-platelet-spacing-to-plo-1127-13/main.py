import math

WAVELENGTHS = {"R": 650.0, "G": 530.0, "B": 450.0}  # nanometers
N_LAYERS = 4
REFRACTIVE = 1.5
ANGLE_DEG = 20.0


def brightness(spacing_nm, wavelength_nm):
    """Reflected intensity (0..1) for a stack of layers."""
    theta = math.radians(ANGLE_DEG)
    sin_t = math.sin(theta) / REFRACTIVE
    cos_t = math.sqrt(1.0 - sin_t * sin_t)
    phase = 4.0 * math.pi * REFRACTIVE * spacing_nm * cos_t / wavelength_nm
    half = phase / 2.0
    s = math.sin(half)
    if abs(s) < 1e-9:
        return 1.0
    ratio = math.sin(N_LAYERS * half) / (N_LAYERS * s)
    return ratio * ratio


def bar(value, width=20):
    n = int(round(value * width))
    return "#" * n + "." * (width - n)


def main():
    print("Platelet spacing vs shimmer brightness")
    print("Layers: %d, angle: %.0f deg, n = %.2f" % (N_LAYERS, ANGLE_DEG, REFRACTIVE))
    print("-" * 78)
    print("%8s  %-22s %-22s %-22s %s" % ("gap(nm)", "R", "G", "B", "dominant"))
    best_total = 0.0
    best_gap = 0
    for gap in range(100, 421, 10):
        vals = {k: brightness(gap, w) for k, w in WAVELENGTHS.items()}
        top = max(vals, key=vals.get)
        dom = top if vals[top] > 0.15 else "-"
        total = sum(vals.values())
        if total > best_total:
            best_total, best_gap = total, gap
        print("%8d  %-22s %-22s %-22s %s" % (
            gap, bar(vals["R"]), bar(vals["G"]), bar(vals["B"]), dom))
    print("-" * 78)
    print("Brightest overall shimmer at gap = %d nm" % best_gap)


if __name__ == "__main__":
    main()
