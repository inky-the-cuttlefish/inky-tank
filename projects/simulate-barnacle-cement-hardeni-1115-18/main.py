import random

random.seed(7)

WIDTH = 40
LAYERS = 6
# Hardness stages: liquid -> gel -> tacky -> firm -> rock-hard
STAGES = "~.:+#"
STAGE_NAMES = ["wet", "gel", "tacky", "firm", "HARD"]


def rock_surface():
    chars = "_,.-_"
    return "".join(random.choice(chars) for _ in range(WIDTH))


def render(layers, rock):
    lines = []
    for row in reversed(layers):
        lines.append("|" + "".join(STAGES[v] if v >= 0 else " " for v in row) + "|")
    lines.append("+" + rock + "+")
    return "\n".join(lines)


def cure(layers):
    for r_index, r in enumerate(layers):
        # lower layers (small index) harden faster
        age = len(layers) - 1 - r_index
        chance = max(0.9 - 0.1 * age, 0.3)
        for i in range(WIDTH):
            if 0 <= r[i] < len(STAGES) - 1 and random.random() < chance:
                r[i] += 1


def main():
    rock = rock_surface()
    layers = []
    print("=== Barnacle Cement Simulator ===")
    print("Legend: " + ", ".join(
        "'%s'=%s" % (STAGES[i], STAGE_NAMES[i]) for i in range(len(STAGES))))
    print()

    for n in range(1, LAYERS + 1):
        # Secrete a new wet layer, narrowing toward the top
        margin = n - 1 if n < 5 else 4
        margin += random.randint(0, 1)
        row = [-1] * WIDTH
        for i in range(margin * 2, WIDTH - margin * 2):
            row[i] = 0
        layers.append(row)

        print("--- Secretion %d: barnacle oozes fresh cement ---" % n)
        print(render(layers, rock))
        print("    ...curing...")
        cure(layers)
        print(render(layers, rock))
        print()

    # Let everything finish hardening
    rounds = 0
    while any(0 <= v < len(STAGES) - 1 for r in layers for v in r):
        cure(layers)
        rounds += 1
    print("--- Fully cured after %d more rounds ---" % rounds)
    print(render(layers, rock))
    print("The barnacle is stuck for life!")


if __name__ == "__main__":
    main()
