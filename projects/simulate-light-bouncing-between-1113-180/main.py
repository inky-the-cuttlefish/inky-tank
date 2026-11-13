import random

random.seed(7)

# Wavelength bands (nm) with slightly different refractive-like reflectivity.
BANDS = [
    ("Red    650", 0.30),
    ("Orange 600", 0.31),
    ("Yellow 580", 0.32),
    ("Green  530", 0.33),
    ("Cyan   490", 0.34),
    ("Blue   450", 0.35),
    ("Violet 410", 0.36),
]

LAYERS = 12          # stacked platelet layers
PHOTONS = 4000       # photons per band
ABSORB = 0.002       # tiny absorption per interaction
MAX_STEPS = 400


def trace(reflectivity):
    """Return True if photon exits back out the top (reflected)."""
    depth = 0      # 0 = just above the first layer
    direction = 1  # +1 going down, -1 going up
    for _ in range(MAX_STEPS):
        if random.random() < ABSORB:
            return False
        # Photon meets an interface between layers.
        if direction == 1:
            if random.random() < reflectivity:
                direction = -1
                depth -= 1
            else:
                depth += 1
        else:
            if random.random() < reflectivity:
                direction = 1
                depth += 1
            else:
                depth -= 1
        if depth < 0:
            return True
        if depth >= LAYERS:
            return False
    return False


def bar(frac, width=40):
    n = int(round(frac * width))
    return "#" * n + "." * (width - n)


print("=" * 62)
print(" Shimmering White: light bouncing in stacked platelet layers")
print("=" * 62)
print(" Layers: %d   Photons per band: %d" % (LAYERS, PHOTONS))
print()

results = []
for name, refl in BANDS:
    hits = sum(trace(refl) for _ in range(PHOTONS))
    frac = hits / PHOTONS
    results.append(frac)
    print(" %s |%s| %5.1f%%" % (name, bar(frac), frac * 100))

print()
spread = (max(results) - min(results)) * 100
print(" Spread between bands: %.1f%%" % spread)
print(" Nearly every color bounces back about equally,")
print(" so the mix reaches your eye as bright, shimmering white.")
