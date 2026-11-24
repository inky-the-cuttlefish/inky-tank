import math

# Thin-film interference: reflected intensity for each wavelength
# depends on film thickness. We compute R, G, B intensities and
# map the dominant color to an ASCII character.

WAVELENGTHS = {"R": 650.0, "G": 530.0, "B": 460.0}  # nanometers
N_FILM = 1.33  # refractive index of soapy water


def reflect(thickness_nm, wavelength_nm, angle_deg):
    theta = math.radians(angle_deg)
    # Snell's law: angle inside the film
    sin_t = math.sin(theta) / N_FILM
    cos_t = math.sqrt(1 - sin_t * sin_t)
    # Phase difference (with a half-wave shift from one reflection)
    delta = 4 * math.pi * N_FILM * thickness_nm * cos_t / wavelength_nm
    return 0.5 * (1 - math.cos(delta + math.pi))


def pick_char(r, g, b):
    top = max(r, g, b)
    if top < 0.25:
        return " "  # dark, destructive interference
    if min(r, g, b) > 0.7 * top and top > 0.7:
        return "#"  # near white
    if r >= g and r >= b:
        return "R" if g < 0.5 * r else "o"  # red or orange/yellow
    if g >= r and g >= b:
        return "G" if b < 0.5 * g else "~"
    return "B" if r < 0.5 * b else "v"  # blue or violet


def main():
    print("Thin-film shimmer map")
    print("Legend: R red  o orange  G green  ~ cyan  B blue  v violet  # white")
    print("Rows: viewing angle (deg).  Columns: film thickness 50 -> 900 nm")
    print()
    angles = [0, 15, 30, 45, 60, 75]
    thicknesses = [50 + i * 10 for i in range(86)]
    for a in angles:
        row = []
        for t in thicknesses:
            r = reflect(t, WAVELENGTHS["R"], a)
            g = reflect(t, WAVELENGTHS["G"], a)
            b = reflect(t, WAVELENGTHS["B"], a)
            row.append(pick_char(r, g, b))
        print("%3d | %s" % (a, "".join(row)))


if __name__ == "__main__":
    main()
