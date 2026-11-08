# Bird vs human flower visibility simulator (stdlib only, ASCII output)
import math

# Each color: (UV, Blue, Green, Red) reflectance 0..1
# Humans cannot see the UV channel at all.
BACKGROUND = ("Green leaves", (0.05, 0.10, 0.45, 0.15))

FLOWERS = [
    ("Daisy (white)",      (0.05, 0.90, 0.90, 0.90)),
    ("Poppy (red)",        (0.60, 0.05, 0.10, 0.90)),
    ("Buttercup (yellow)", (0.02, 0.10, 0.80, 0.85)),
    ("Sunflower (UV tip)", (0.80, 0.10, 0.75, 0.80)),
    ("Violet (purple)",    (0.40, 0.70, 0.10, 0.40)),
    ("Leaf-green flower",  (0.05, 0.10, 0.45, 0.16)),
    ("Evening primrose",   (0.90, 0.20, 0.70, 0.70)),
]


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def human_view(c):
    # Humans: drop UV channel, keep B, G, R
    return c[1:]


def bird_view(c):
    return c


def bar(value, scale=24):
    n = int(round(min(value, 1.5) / 1.5 * scale))
    return "#" * n


def verdict(d):
    if d < 0.10:
        return "hidden"
    if d < 0.50:
        return "visible"
    if d < 0.90:
        return "striking"
    return "POPS!"


def main():
    bg_name, bg = BACKGROUND
    print("=" * 62)
    print(" BIRD vs HUMAN: who spots the flowers against " + bg_name + "?")
    print("=" * 62)
    print(" Bird sees 4 channels (UV,B,G,R). Human sees 3 (B,G,R).")
    print("-" * 62)

    bird_wins = []
    for name, col in FLOWERS:
        h = distance(human_view(col), human_view(bg))
        b = distance(bird_view(col), bird_view(bg))
        print(" " + name)
        print("   human: %-24s %.2f %s" % (bar(h), h, verdict(h)))
        print("   bird : %-24s %.2f %s" % (bar(b), b, verdict(b)))
        if b - h > 0.15:
            bird_wins.append(name)
        print()

    print("-" * 62)
    if bird_wins:
        print(" Flowers birds notice much better than we do:")
        for n in bird_wins:
            print("   * " + n)
    else:
        print(" No flower gives birds a big edge.")
    print(" Moral: UV is a secret channel only birds can read.")


if __name__ == "__main__":
    main()
