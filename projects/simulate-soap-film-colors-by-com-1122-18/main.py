import math

# Thin-film interference for a soap film (n ~ 1.33) in air.
# Front surface reflection has a half-wave phase shift, the back does not,
# so reflectance ~ sin^2(2*pi*n*d/lambda).

N_FILM = 1.33
WAVELENGTHS = {"R": 650.0, "G": 530.0, "B": 450.0}  # nanometers


def reflectance(thickness_nm, wavelength_nm):
    phase = 2.0 * math.pi * N_FILM * thickness_nm / wavelength_nm
    return math.sin(phase) ** 2


def bar(value, width=20):
    filled = int(round(value * width))
    return "#" * filled + "." * (width - filled)


def dominant(r, g, b):
    top = max(r, g, b)
    if top < 0.08:
        return "dark"
    if abs(r - g) < 0.1 and abs(g - b) < 0.1 and top > 0.85:
        return "white"
    if r > 0.7 and g > 0.7 and b < 0.4:
        return "yellow"
    if r > 0.7 and b > 0.7 and g < 0.4:
        return "magenta"
    if g > 0.7 and b > 0.7 and r < 0.4:
        return "cyan"
    if top == r:
        return "red"
    if top == g:
        return "green"
    return "blue"


def main():
    print("SOAP FILM INTERFERENCE (wedge, thin at top, thick at bottom)")
    print("n = %.2f   R=650nm  G=530nm  B=450nm" % N_FILM)
    print()
    print("%6s  %-20s %-20s %-20s  %s" % ("nm", "Red", "Green", "Blue", "Look"))
    print("-" * 82)
    for d in range(0, 801, 25):
        r = reflectance(d, WAVELENGTHS["R"])
        g = reflectance(d, WAVELENGTHS["G"])
        b = reflectance(d, WAVELENGTHS["B"])
        print("%6d  %s %s %s  %s" % (d, bar(r), bar(g), bar(b),
                                     dominant(r, g, b)))


if __name__ == "__main__":
    main()
