import random

random.seed()

SUCKERS = ["Bob", "Alice", "Greg", "Mimi", "Dewey", "Pam", "Larry", "Zelda"]

ROCKS = ["granite", "basalt", "limestone", "quartz", "pumice", "obsidian"]

FLAVORS = [
    "lemon", "burnt toast", "old pennies", "wet dog", "blueberry",
    "cold soup", "pencil eraser", "mild regret", "mint", "chalk",
    "dusty attic", "pickle juice", "lukewarm tea", "birthday cake",
]

REACTIONS = [
    "squints thoughtfully",
    "gags a little",
    "nods with confidence",
    "raises one eyebrow",
    "looks deeply betrayed",
    "smiles far too much",
]

NOTES = [
    "with a hint of {}",
    "with a finish of {}",
    "followed by an aftertaste of {}",
    "with undertones of {}",
]


def taste(name, rock):
    main = random.choice(FLAVORS)
    extra = random.choice([f for f in FLAVORS if f != main])
    reaction = random.choice(REACTIONS)
    note = random.choice(NOTES).format(extra)
    print(f"{name} licks the {rock} and {reaction}.")
    print(f"  {name}: \"Definitely {main}, {note}.\"")
    return main


def main():
    rock = random.choice(ROCKS)
    print("=" * 44)
    print("   THE GREAT ROCK TASTING EXPERIMENT")
    print("=" * 44)
    print(f"Today's rock: {rock.upper()}")
    print("(It is, scientifically, just a rock.)\n")

    votes = {}
    for name in SUCKERS:
        flavor = taste(name, rock)
        votes[flavor] = votes.get(flavor, 0) + 1
        print()

    print("-" * 44)
    print("RESULTS:")
    ranked = sorted(votes.items(), key=lambda kv: (-kv[1], kv[0]))
    for flavor, count in ranked:
        print(f"  {flavor}: {'*' * count} ({count})")

    top_flavor, top_count = ranked[0]
    if top_count > 1:
        print(f"\nConsensus: it tastes like {top_flavor}.")
    else:
        print("\nNo consensus. Everyone tasted something different.")
    print("Conclusion: it is still just a rock.")


if __name__ == "__main__":
    main()
