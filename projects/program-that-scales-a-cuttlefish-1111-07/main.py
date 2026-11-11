# Cuttlefish scaler: draws an ASCII cuttlefish at growing sizes.
# Stdlib only, no files, no network.

STAGES = [
    ("Hatchling", 2, "about the size of a jellybean (~1 cm)"),
    ("Juvenile", 5, "about the size of a banana (~15 cm)"),
    ("Adult common cuttlefish", 8, "about the size of a football (~30 cm)"),
    ("Giant cuttlefish", 12, "mantle up to ~50 cm, over 1 m with arms"),
]


def draw_cuttlefish(scale):
    """Build a cuttlefish whose body width and tentacle count scale up."""
    body_w = scale * 2
    lines = []

    # fin ruffle along the top, aligned with the body interior
    lines.append(" " + "~" * (body_w + 2))

    # body (mantle) rows
    rows = max(2, scale // 2)
    for i in range(rows):
        fill = "=" if i % 2 == 0 else "-"
        lines.append("(" + fill * (body_w + 2) + ")")

    # eyes row
    eye_gap = " " * max(1, body_w - 2)
    lines.append(" " + "O" + eye_gap + "O")

    # tentacles
    count = max(3, scale // 2 + 2)
    lines.append(" " + "/|" * count)
    lines.append(" " + "\\ " * count)
    return lines


def main():
    print("=" * 50)
    print("  HOW BIG DO GIANT CUTTLEFISH GROW?")
    print("=" * 50)
    for name, scale, note in STAGES:
        print()
        print("--- " + name + " (scale x" + str(scale) + ") ---")
        for line in draw_cuttlefish(scale):
            print(line)
        print("Size: " + note)

    print()
    print("Fun fact: giant cuttlefish (Sepia apama) are the largest "
          "cuttlefish species in the world!")


if __name__ == "__main__":
    main()
