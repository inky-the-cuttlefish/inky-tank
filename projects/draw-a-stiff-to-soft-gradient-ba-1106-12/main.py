# Beak hardness gradient: stiff tip to soft base (ASCII only, stdlib only)

# Characters ordered from lightest (soft) to densest (stiff)
RAMP = " .:-=+*#%@"

# Layers from tip to base, with a made-up hardness value (0-100)
LAYERS = [
    ("Tip (rostrum)", 100),
    ("Hard crest", 85),
    ("Upper wall", 68),
    ("Mid wall", 50),
    ("Lower wall", 32),
    ("Base joint", 15),
    ("Buccal membrane", 3),
]

BAR_WIDTH = 40


def shade(value):
    """Map a 0-100 hardness value to a ramp character."""
    idx = int(round(value / 100 * (len(RAMP) - 1)))
    return RAMP[idx]


def gradient_bar(width):
    """Build one continuous bar going from stiff (left) to soft (right)."""
    chars = []
    for i in range(width):
        value = 100 - (i / (width - 1)) * 100
        chars.append(shade(value))
    return "".join(chars)


def layer_row(name, value):
    filled = max(1, int(round(value / 100 * BAR_WIDTH)))
    bar = shade(value) * filled
    return "%-17s |%-*s| %3d" % (name, BAR_WIDTH, bar, value)


def main():
    title = "BEAK HARDNESS GRADIENT"
    print("=" * 62)
    print(title.center(62).rstrip())
    print("=" * 62)
    print()
    print("Overall gradient (stiff -> soft):")
    print("STIFF [" + gradient_bar(BAR_WIDTH) + "] SOFT")
    print()
    print("Layer by layer:")
    print("-" * 62)
    for name, value in LAYERS:
        print(layer_row(name, value))
    print("-" * 62)
    print()
    print("Scale: [" + RAMP + "]  (soft -> stiff)")
    print()
    print("Fun fact: the squid beak is stiff at the tip and soft at the")
    print("base, which keeps it from tearing the soft tissue around it!")


if __name__ == "__main__":
    main()
