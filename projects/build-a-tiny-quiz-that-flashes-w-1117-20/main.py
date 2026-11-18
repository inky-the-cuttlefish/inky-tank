import random

# (creature, makes its own light?, fun fact)
CREATURES = [
    ("Firefly", True, "Uses luciferin and luciferase to flash light."),
    ("Anglerfish", True, "Glowing lure is lit by helpful bacteria."),
    ("Cat", False, "Eyes shine only by reflecting light."),
    ("Jellyfish (Aequorea)", True, "Glows green using a special protein."),
    ("Goldfish", False, "Pretty, but not bioluminescent."),
    ("Vampire Squid", True, "Shoots glowing mucus to confuse enemies."),
    ("Moon", False, "Only reflects sunlight."),
    ("Glow Worm", True, "Dangles glowing threads to trap prey."),
    ("Owl", False, "Great night vision, zero glow."),
    ("Dinoflagellate", True, "Makes ocean waves sparkle blue at night."),
]

FLASH = ["*", "+", "o", "O", "0", "O", "o", "+", "*"]


def flash_bar():
    return " ".join(FLASH)


def main():
    random.seed(42)  # fixed seed so the output is repeatable
    questions = CREATURES[:]
    random.shuffle(questions)

    print("=" * 44)
    print("   GLOW OR NO GLOW? A BIOLUMINESCENCE QUIZ")
    print("=" * 44)
    print()

    score = 0
    for number, (name, glows, fact) in enumerate(questions, 1):
        # The "player" is a simulated guesser with a fixed lucky streak
        guess = random.random() < 0.5 if number % 3 == 0 else glows
        correct = guess == glows
        score += correct

        print("Q%d: Does the %s make its own light?" % (number, name))
        print("    " + flash_bar())
        print("    Guess : %s" % ("GLOWS" if guess else "NO GLOW"))
        print("    Answer: %s  [%s]" % (
            "GLOWS" if glows else "NO GLOW",
            "right" if correct else "oops"))
        print("    Fact  : " + fact)
        print()

    total = len(questions)
    print("-" * 44)
    print("Final score: %d / %d" % (score, total))

    if score == total:
        title = "Deep Sea Legend"
    elif score >= total * 0.7:
        title = "Glow Expert"
    else:
        title = "Needs More Night Dives"
    print("Your title: " + title)
    print()
    print("      .  *  .    *   .  *")
    print("   *    .   (glow!)  .    *")
    print("      .   *    .   *   .")


if __name__ == "__main__":
    main()