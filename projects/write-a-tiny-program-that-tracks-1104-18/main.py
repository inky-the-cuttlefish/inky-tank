import random

random.seed(42)

BACTERIA = ["Lactobacillus", "E. coli", "Bacillus", "Clostridium"]
NAMES = ["Pip", "Fluffy", "Nugget", "Biscuit", "Peep"]
HOURS = 6


def colonize(colony, hours):
    """Each hour, new bacteria arrive and existing ones multiply."""
    history = []
    for hour in range(1, hours + 1):
        # existing colonies grow
        for species in list(colony):
            growth = random.uniform(1.2, 2.0)
            colony[species] = int(colony[species] * growth)
        # new arrivals from the environment
        for _ in range(random.randint(1, 3)):
            species = random.choice(BACTERIA)
            colony[species] = colony.get(species, 0) + random.randint(5, 30)
        history.append((hour, sum(colony.values())))
    return history


def bar(value, scale=50):
    return "#" * max(1, value // scale)


def main():
    print("=== Hatchling Microbiome Tracker ===")
    totals = {}
    for name in NAMES:
        colony = {}
        history = colonize(colony, HOURS)
        totals[name] = sum(colony.values())
        print("\nHatchling: " + name)
        for hour, count in history:
            print("  hour %d | %-30s %d" % (hour, bar(count)[:30], count))
        dominant = max(colony, key=colony.get)
        print("  dominant species: " + dominant)

    print("\n=== Final Leaderboard (most colonized) ===")
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    for rank, (name, total) in enumerate(ranked, 1):
        print("  %d. %-8s %d bacteria" % (rank, name, total))


if __name__ == "__main__":
    main()
