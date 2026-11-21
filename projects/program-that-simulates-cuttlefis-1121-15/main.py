import random

random.seed(7)

PATTERNS = {
    "calm":     ("....", "Smooth pale skin"),
    "curious":  ("~~~~", "Gentle rippling waves"),
    "alarmed":  ("####", "Dark flash"),
    "flirty":   ("=-=-", "Zebra stripes"),
    "camo":     (":;:;", "Mottled blend with the rocks"),
}

MOODS = list(PATTERNS.keys())

# How a cuttlefish tends to react when it sees a neighbor's mood.
REACTIONS = {
    "calm":    {"calm": 0.6, "curious": 0.3, "camo": 0.1},
    "curious": {"curious": 0.5, "calm": 0.2, "flirty": 0.3},
    "alarmed": {"alarmed": 0.5, "camo": 0.4, "calm": 0.1},
    "flirty":  {"flirty": 0.4, "curious": 0.4, "alarmed": 0.2},
    "camo":    {"camo": 0.6, "calm": 0.3, "curious": 0.1},
}


def pick(weights):
    r = random.random()
    total = 0.0
    mood = None
    for mood, w in weights.items():
        total += w
        if r <= total:
            return mood
    return mood


class Cuttlefish:
    def __init__(self, name):
        self.name = name
        self.mood = random.choice(MOODS)

    def skin(self):
        return PATTERNS[self.mood][0] * 3


def show(rnd, group):
    print("--- Round %d ---" % rnd)
    for c in group:
        print("%-7s [%s] %-8s %s" % (c.name, c.skin(), c.mood, PATTERNS[c.mood][1]))
    print()


def main():
    print("CUTTLEFISH MOOD RING: skin signals in the reef\n")
    group = [Cuttlefish(n) for n in ("Inky", "Sepia", "Marble", "Flash")]
    for rnd in range(1, 6):
        show(rnd, group)
        # Everyone watches a random neighbor, then all update at once.
        new_moods = []
        for c in group:
            neighbor = random.choice([o for o in group if o is not c])
            new_moods.append(pick(REACTIONS[neighbor.mood]))
        for c, m in zip(group, new_moods):
            c.mood = m
    print("The reef settles. Glub!")


if __name__ == "__main__":
    main()
