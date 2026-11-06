import random

random.seed(520)

EPOCHS = [
    ("Terreneuvian", 4),
    ("Series 2", 5),
    ("Miaolingian", 6),
    ("Furongian", 5),
]

PREFIXES = ["Olen", "Redli", "Para", "Elra", "Pagu", "Ptych", "Asaph", "Cory", "Hydro", "Ampy"]
SUFFIXES = ["ellus", "chia", "doxides", "thia", "ites", "opsis", "aspis", "pyge"]
RAYS = "*+.o'`"


def make_name(existing):
    for _ in range(50):
        n = random.choice(PREFIXES) + random.choice(SUFFIXES)
        if n not in existing:
            return n
    return None


def burst(size):
    """ASCII firework; radius scales with diversity (1..5)."""
    r = max(1, min(size // 4, 5))
    pad = r * 2 + 2
    lines = [" " * pad + "|"]
    for i in range(r, 0, -1):
        ray = random.choice(RAYS)
        lines.append(" " * (pad - i * 2) + ray + " " * (i * 4 - 1) + ray)
    lines.append(" " * (pad - 1) + "-*-")
    for i in range(1, r + 1):
        ray = random.choice(RAYS)
        lines.append(" " * (pad - i * 2) + ray + " " * (i * 4 - 1) + ray)
    return "\n".join(lines)


def main():
    species = [make_name([])]
    print("=== CAMBRIAN TRILOBITE FIREWORKS ===")
    for epoch, steps in EPOCHS:
        print("\n--- " + epoch + " epoch ---")
        for step in range(1, steps + 1):
            born = []
            for _ in list(species):
                if random.random() < 0.35 and len(species) + len(born) < 40:
                    c = make_name(species + born)
                    if c:
                        born.append(c)
            species.extend(born)
            lost = 0
            for sp in list(species):
                if len(species) > 1 and random.random() < 0.2:
                    species.remove(sp)
                    lost += 1
            print("Step %d: +%d born, -%d extinct, diversity = %d"
                  % (step, len(born), lost, len(species)))
            print(burst(len(species)))
            if born:
                print("   BOOM! New lineage: " + born[-1])
    print("\nSurvivors: " + ", ".join(sorted(species)))


main()
