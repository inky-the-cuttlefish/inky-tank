import random

random.seed(7)

# Rough, illustrative numbers (order-of-magnitude, not lab-exact)
SPATULAE_PER_TOE = 10_000_000   # ~1e8 total across toes, simplified
TOES = 10
SPATULA_FORCE_NN = 40.0         # nanonewtons per spatula at ideal contact
GRAVITY = 9.81

WALLS = {"glass": 0.85, "smooth tile": 0.8, "painted wall": 0.6,
         "dusty brick": 0.25, "wet glass": 0.1}


def grip_force_newtons(q):
    total_nn = 0.0
    for _ in range(TOES):
        toe_q = max(0.0, min(1.0, random.gauss(q, 0.08)))
        touching = SPATULAE_PER_TOE * toe_q * random.uniform(0.95, 1.05)
        total_nn += touching * SPATULA_FORCE_NN
    return total_nn * 1e-9  # nN -> N


def bar(value, scale, width=30):
    n = int(max(0, min(width, value / scale * width)))
    return "#" * n + "." * (width - n)


def main():
    mass = 0.05
    weight = mass * GRAVITY
    print("=== GECKO GRIP SIMULATOR ===")
    print("Gecko mass: %.0f g, weight: %.2f N" % (mass * 1000, weight))
    print("Toes: %d, spatulae per toe: %d" % (TOES, SPATULAE_PER_TOE))
    print()
    results = []
    for wall, q in WALLS.items():
        f = grip_force_newtons(q)
        ratio = f / weight
        results.append((wall, f, ratio))
        print("%-13s [%s] %6.2f N  x%.1f body weight" %
              (wall, bar(f, weight * 10), f, ratio))
        if ratio >= 1:
            print("              -> HOLDS! Gecko clings happily.")
        else:
            print("              -> SLIP! Gecko slides down.")
    print()
    best = max(results, key=lambda r: r[1])
    print("Best grip: %s. Tiny forces, huge numbers!" % best[0])


if __name__ == "__main__":
    main()
