import random

WIDTH = 60
FISH = 14
STEPS = 40
SEED = 7


def spread(positions):
    # Average distance from the mean position (lower = more gathered)
    mean = sum(positions) / len(positions)
    return sum(abs(p - mean) for p in positions) / len(positions)


def step(positions, mood):
    new = []
    for i, p in enumerate(positions):
        others = [q for j, q in enumerate(positions) if j != i]
        nearest = min(others, key=lambda q: abs(q - p))
        direction = 0
        if nearest > p:
            direction = 1
        elif nearest < p:
            direction = -1
        if mood == "shy":
            direction = -direction
        # random wiggle so it isn't boring
        move = direction if random.random() < 0.7 else random.choice([-1, 0, 1])
        new.append(max(0, min(WIDTH - 1, p + move)))
    return new


def draw(positions):
    row = ["."] * WIDTH
    for p in positions:
        row[p] = "@" if row[p] == "." else "#"
    return "".join(row)


def run(mood):
    random.seed(SEED)
    positions = [random.randrange(WIDTH) for _ in range(FISH)]
    start = spread(positions)
    print("=== %s cuttlefish ===" % mood.upper())
    for t in range(STEPS + 1):
        if t % 10 == 0:
            print("t=%02d %s" % (t, draw(positions)))
        if t < STEPS:
            positions = step(positions, mood)
    end = spread(positions)
    verdict = "GATHERED" if end < start else "SCATTERED"
    print("spread: %.1f -> %.1f  => %s" % (start, end, verdict))
    print()


if __name__ == "__main__":
    print("Cuttlefish Crowd Simulator  (@ = fish, # = pile-up)")
    print()
    run("social")
    run("shy")
