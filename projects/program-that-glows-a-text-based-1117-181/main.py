import time

CREATURES = {
    "octopus": [
        "   ,-''''-.   ",
        "  (  o  o  )  ",
        "   \\  __  /   ",
        "  /|/|/|\\|\\   ",
        " (_/ /  \\ \\_) ",
    ],
    "fish": [
        "      ,--.      ",
        "  ><(((o> ~     ",
        "      `--'      ",
    ],
    "jellyfish": [
        "   .-''''-.   ",
        "  (  o  o  )  ",
        "   '-.__.-'   ",
        "   | | | |    ",
        "   ) ( ) (    ",
    ],
    "crab": [
        " \\\\(o)___(o)// ",
        "   /  ___  \\   ",
        "  /_/|_|_|\\_\\  ",
    ],
    "whale": [
        "        .-----.      ",
        "  _____/  o    \\__   ",
        " (______________  >< ",
        "     ~  ~  ~  ~      ",
    ],
}

GLOW = ["-", "=", "#", "=", "-"]


def panel(name, art, phase):
    width = max(len(line) for line in art) + 4
    edge = GLOW[phase % len(GLOW)]
    side = GLOW[(phase + 2) % len(GLOW)]
    top = "+" + edge * (width - 2) + "+"
    lines = [top]
    title = name.upper().center(width - 4)
    lines.append(side + " " + title + " " + side)
    lines.append(side + " " + " " * (width - 4) + " " + side)
    for row in art:
        lines.append(side + " " + row.ljust(width - 4) + " " + side)
    lines.append(top)
    return "\n".join(lines)


def show(name):
    key = name.strip().lower()
    if key not in CREATURES:
        print("Unknown creature '%s'. Try: %s" % (name, ", ".join(sorted(CREATURES))))
        return
    for phase in range(5):
        print(panel(key, CREATURES[key], phase))
        print("   *glow level %d*" % (phase + 1))
        time.sleep(0.15)


def main():
    demo_inputs = ["octopus", "jellyfish", "kraken", "whale"]
    for typed in demo_inputs:
        print("\nType a sea creature> " + typed)
        show(typed)
    print("\nSwim safe! Edit demo_inputs or swap in input() to play.")


main()