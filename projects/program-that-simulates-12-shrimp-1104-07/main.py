import math

# Mantis shrimp have 12 photoreceptor channels. Each one is modeled here as
# a bell curve peaked at a particular wavelength (in nanometers).
CHANNELS = [
    ("UV-1", 320), ("UV-2", 350), ("UV-3", 380), ("Violet", 420),
    ("Indigo", 450), ("Blue", 480), ("Cyan", 510), ("Green", 540),
    ("Lime", 570), ("Yellow", 600), ("Orange", 630), ("Red", 680),
]

# ASCII shading characters, from weak to strong signal
SHADES = " .:-=+*#%@"


def response(wavelength, peak, width=28.0):
    """Gaussian sensitivity of one channel to a wavelength."""
    return math.exp(-((wavelength - peak) ** 2) / (2 * width ** 2))


def shade(value):
    idx = int(value * (len(SHADES) - 1))
    return SHADES[max(0, min(idx, len(SHADES) - 1))]


def dominant_name(wavelength):
    best = max(CHANNELS, key=lambda c: response(wavelength, c[1]))
    return best[0]


def main():
    print("=== Mantis Shrimp 12-Channel Rainbow Mixer ===\n")

    start, end, step = 300, 700, 5
    waves = list(range(start, end + 1, step))
    print("Channel sensitivity (300nm -> 700nm):")
    for name, peak in CHANNELS:
        row = "".join(shade(response(w, peak)) for w in waves)
        print("%-7s|%s|" % (name, row))

    print("\nMixed palette (sum of all 12 channels):")
    totals = [sum(response(w, peak) for _, peak in CHANNELS) for w in waves]
    top = max(totals)
    row = "".join(shade(t / top) for t in totals)
    print("%-7s|%s|" % ("Mix", row))

    # Axis marks every 50nm (each character is 5nm)
    axis = [" "] * len(waves)
    labels = ""
    for i, w in enumerate(waves):
        if w % 100 == 0:
            axis[i] = "|"
    print("%-7s %s" % ("", "".join(axis)))
    print("        300nm       400nm       500nm       600nm       700nm"
          .replace("       ", "  ", 0))

    print("\nWhich channel leads at key wavelengths:")
    for w in (350, 420, 480, 540, 600, 680):
        print("  %dnm -> %s" % (w, dominant_name(w)))

    print("\nTwelve channels, one rainbow. Nice work, shrimp!")


if __name__ == "__main__":
    main()
