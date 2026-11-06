# Cuttlebone buoyancy simulator: chambers trade water for gas until the
# cuttlefish hovers level. Pure stdlib, prints ASCII only.

CHAMBERS = 8          # chambers from head (front) to tail (back)
TARGET_DEPTH = 5.0    # desired depth in meters


def make_chambers():
    # Start nose-heavy: front chambers flooded, back chambers gassy,
    # so the cuttlefish pitches nose-down and sinks.
    return [0.9, 0.8, 0.7, 0.5, 0.4, 0.3, 0.2, 0.1]  # water fraction


def buoyancy(chambers):
    # More gas (less water) = more lift; 0 means neutral
    gas = sum(1.0 - w for w in chambers)
    return gas - CHAMBERS * 0.5


def tilt(chambers):
    # Front-half gas minus back-half gas; positive = nose up
    half = CHAMBERS // 2
    front = sum(1.0 - w for w in chambers[:half])
    back = sum(1.0 - w for w in chambers[half:])
    return front - back


def draw(step, chambers, depth):
    bar = ""
    for w in chambers:
        level = int(round(w * 4))
        bar += "[" + "~" * level + "." * (4 - level) + "]"
    t = tilt(chambers)
    if abs(t) < 0.1:
        pose = "  ~(o_o)~   level"
    elif t > 0:
        pose = "   /(o_o)    nose up"
    else:
        pose = "   \\(o_o)    nose down"
    print("Step %2d depth %4.1fm" % (step, depth))
    print("  " + bar)
    print(pose)
    print("")


def adjust(chambers, depth):
    # Pump water out of the front, into the back, to level the body;
    # then trim overall gas depending on whether we are too deep or shallow.
    half = CHAMBERS // 2
    t = tilt(chambers)
    shift = max(-0.1, min(0.1, t * 0.1))
    for i in range(CHAMBERS):
        # nose down (t<0): drain front water, flood back a bit
        chambers[i] += shift if i < half else -shift
    err = depth - TARGET_DEPTH
    trim = max(-0.05, min(0.05, err * 0.01))
    for i in range(CHAMBERS):
        chambers[i] -= trim
    for i in range(CHAMBERS):
        chambers[i] = max(0.0, min(1.0, chambers[i]))


def main():
    chambers = make_chambers()
    depth = 8.0
    print("=== Cuttlebone Buoyancy Tuner ===")
    print("~ = water, . = gas\n")
    for step in range(1, 21):
        draw(step, chambers, depth)
        depth -= buoyancy(chambers) * 0.5
        depth = max(0.0, depth)
        adjust(chambers, depth)
        if abs(depth - TARGET_DEPTH) < 0.3 and abs(tilt(chambers)) < 0.1:
            draw(step + 1, chambers, depth)
            print("Level and hovering. Inky is happy!")
            return
    print("Still bobbing after 20 steps. Inky shrugs.")


if __name__ == "__main__":
    main()
