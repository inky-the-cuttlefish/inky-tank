import math

BANDS = [
    ("R", "red", 650),
    ("O", "orange", 600),
    ("Y", "yellow", 580),
    ("G", "green", 540),
    ("C", "cyan", 490),
    ("B", "blue", 460),
    ("V", "violet", 420),
]

PLATES = 6
WIDTH = 48
N_FILM = 1.45
DULL = 0.55


def reflectance(wavelength, thickness, angle_deg):
    """Toy thin-film interference."""
    theta = math.radians(angle_deg)
    sin_t = math.sin(theta) / N_FILM
    cos_t = math.sqrt(max(0.0, 1.0 - sin_t * sin_t))
    path = 2.0 * N_FILM * thickness * cos_t
    phase = 2.0 * math.pi * path / wavelength
    return 0.5 * (1.0 - math.cos(phase))


def plate_thickness(i, x):
    base = 300 + i * 35
    ripple = 25 * math.sin(x * 0.35 + i)
    return base + ripple


def strip(angle):
    out = []
    for x in range(WIDTH):
        best_sym, best_val = ".", -1.0
        for sym, _name, wl in BANDS:
            total = 0.0
            for p in range(PLATES):
                total += reflectance(wl, plate_thickness(p, x), angle)
            total /= PLATES
            if total > best_val:
                best_sym, best_val = sym, total
        out.append(best_sym if best_val >= DULL else ".")
    return "".join(out)


def main():
    line = "=" * 60
    print(line)
    print("  SHIMMER PLATES: %d stacked reflectors, tilt to see color" % PLATES)
    print(line)
    print("Legend: R O Y G C B V = dominant color, . = dull")
    print()
    for angle in range(0, 70, 10):
        print("tilt %2d deg | %s" % (angle, strip(angle)))


if __name__ == "__main__":
    main()
