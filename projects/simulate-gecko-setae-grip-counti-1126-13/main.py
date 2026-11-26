import random

random.seed(42)

# Rough, illustrative numbers (not precise biology)
GECKO_MASS_G = 50.0
G = 9.81
WEIGHT_N = GECKO_MASS_G / 1000.0 * G

ROWS = 12
COLS = 40
SETAE_PER_CELL = 5000
FORCE_PER_SETA_N = 2e-7
GLASS_ROUGHNESS = 0.35
CONTACT_RANGE = 0.6


def press_foot(pressure):
    """Return (setae in contact, ascii grid) for a given pressure (0..1)."""
    contacts = 0
    grid = []
    for r in range(ROWS):
        row = ""
        for c in range(COLS):
            bump = random.random() * GLASS_ROUGHNESS
            gap = bump * (1.2 - pressure)
            if gap < CONTACT_RANGE * 0.5:
                frac = 1.0 - gap / (CONTACT_RANGE * 0.5)
                contacts += int(SETAE_PER_CELL * frac)
                row += "#" if frac > 0.6 else "+"
            else:
                row += "."
        grid.append(row)
    return contacts, grid


def main():
    print("=== GECKO SETAE GRIP SIMULATOR ===")
    print("Gecko mass: %.0f g, weight: %.3f N" % (GECKO_MASS_G, WEIGHT_N))
    print("Glass wall roughness: %.2f" % GLASS_ROUGHNESS)
    print()

    best = None
    for pressure in (0.2, 0.5, 0.8):
        contacts, grid = press_foot(pressure)
        total = contacts * 4 * FORCE_PER_SETA_N  # four feet
        ratio = total / WEIGHT_N
        print("Pressure %.1f -> %d setae touching (one foot)" % (pressure, contacts))
        print("  Total grip (4 feet): %.3f N  (%.1fx body weight)" % (total, ratio))
        if best is None or contacts > best[0]:
            best = (contacts, pressure, grid, ratio)

    print()
    print("Best footprint (pressure %.1f), # = strong, + = weak, . = none:" % best[1])
    for row in best[2]:
        print("  " + row)
    print()
    if best[3] >= 1.0:
        print("The gecko sticks! Safety margin: %.1fx its weight." % best[3])
    else:
        print("The gecko slips... splat.")


if __name__ == "__main__":
    main()
