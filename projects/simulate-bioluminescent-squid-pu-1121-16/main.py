import math
import time

# Two squid with coupled oscillators that drift into sync.
SHADES = " .:-=+*#%@"
WIDTH = 24
FRAMES = 60


def glow_char(phase):
    b = (math.sin(phase) + 1) / 2
    return SHADES[int(b * (len(SHADES) - 1))], b


def squid(phase):
    ch, b = glow_char(phase)
    spots = ch * 3
    lines = [
        "    ,---.    ",
        "   ( %s )   " % spots,
        "    \\ %s /    " % ch,
        "    |||||    ",
        "   /|/|\\|\\   ",
    ]
    return lines, b


def side_by_side(a, b):
    return ["%s    %s" % (x, y) for x, y in zip(a, b)]


def bar(b):
    n = int(b * WIDTH)
    return "[" + "#" * n + "." * (WIDTH - n) + "]"


def main():
    p1, p2 = 0.0, math.pi * 0.9   # nearly opposite phases
    f1, f2 = 0.55, 0.40           # different natural rhythms
    k = 0.30                      # coupling strength (enough to lock)
    dt = 1.0

    print("Two bioluminescent squid meet in the deep...\n")
    sync = 0.0
    for frame in range(FRAMES):
        d1 = f1 + k * math.sin(p2 - p1)
        d2 = f2 + k * math.sin(p1 - p2)
        p1 += d1 * dt
        p2 += d2 * dt

        a, b1 = squid(p1)
        c, b2 = squid(p2)
        sync = 1 - abs(math.sin((p1 - p2) / 2))

        print("Frame %02d" % frame)
        print("   Inky              Blink")
        for line in side_by_side(a, c):
            print(line)
        print(bar(b1) + " " + bar(b2))
        print("Sync: %3d%%\n" % int(sync * 100))
        time.sleep(0.15)

    if sync > 0.9:
        print("They are flashing in perfect rhythm. Friends!")
    else:
        print("They are still finding each other's rhythm...")


if __name__ == "__main__":
    main()
