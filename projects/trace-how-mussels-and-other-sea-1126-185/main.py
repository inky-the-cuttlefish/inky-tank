import random
import time

random.seed(7)

STAGES = [
    ("Foot probes rock",
     "The mussel extends its foot and presses it to a surface, making a tiny suction cup."),
    ("Secrete proteins",
     "Glands release DOPA-rich proteins (the sticky stuff) plus collagen for the thread."),
    ("Clear the water",
     "Acidic conditions keep DOPA from oxidizing too early, and the surface is cleared of water."),
    ("Metal cross-linking",
     "Iron ions bind DOPA, forming tough links that harden the glue underwater."),
    ("Thread forms",
     "The foot groove acts as a mold: a stretchy-yet-strong byssus thread is cast."),
    ("Plaque sets",
     "The sticky plaque at the end cures and grips the rock."),
]

OTHERS = [
    ("Sandcastle worm", "builds a glue from charged proteins that sets in seawater"),
    ("Barnacle", "secretes a cement that layers over oily films on surfaces"),
    ("Sea star", "uses a two-part glue/de-glue system on its tube feet"),
]


def bar(pct, width=30):
    filled = int(width * pct / 100)
    return "[" + "#" * filled + "." * (width - filled) + "] " + str(pct) + "%"


def main():
    print("=" * 56)
    print("  TRACING UNDERWATER GLUE: THE MUSSEL STORY")
    print("=" * 56)
    total = len(STAGES)
    for i, (name, desc) in enumerate(STAGES, 1):
        pct = int(i * 100 / total)
        print("\nStep %d/%d: %s" % (i, total, name))
        print("  " + desc)
        print("  " + bar(pct))
        time.sleep(0.2)

    strength = random.randint(70, 99)
    print("\nSimulated grip strength: %d%% of a wave's pull" % strength)
    if strength >= 85:
        print("The mussel holds fast through the storm!")
    else:
        print("The mussel wobbles, but it will add more threads.")

    print("\nOther sticky sea animals:")
    for name, how in OTHERS:
        print("  - %s %s." % (name, how))


if __name__ == "__main__":
    main()
