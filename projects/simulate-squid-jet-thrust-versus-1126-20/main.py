import random

random.seed(42)

TRACK = 40
FRAMES_SHOWN = 8


def squid_step(tick):
    # Jet pulse every 4th tick: big burst, then drag during glide.
    if tick % 4 == 0:
        return random.randint(6, 9)
    return random.choice([0, 1, 1, 2])


def gecko_step(tick):
    # Steady climbing, small chance of a grip slip.
    if random.random() < 0.12:
        return -2
    return random.choice([1, 2, 2, 3])


def draw(tick, s, g):
    lane_s = ["~"] * (TRACK + 1)
    lane_g = ["~"] * (TRACK + 1)
    lane_s[TRACK] = "|"
    lane_g[TRACK] = "|"
    s_pos = max(0, min(TRACK, s))
    g_pos = max(0, min(TRACK, g))
    lane_s[s_pos] = "S"
    lane_g[g_pos] = "G"
    print("tick %2d" % tick)
    print("  squid  " + "".join(lane_s))
    print("  gecko  " + "".join(lane_g))
    print()


def main():
    print("=" * 52)
    print("   TINY AQUARIUM RACE: SQUID JET vs GECKO GRIP")
    print("=" * 52)
    print()
    s = g = 0
    tick = 0
    history = []
    while s < TRACK and g < TRACK:
        tick += 1
        s += squid_step(tick)
        g += gecko_step(tick)
        history.append((tick, s, g))

    n = len(history)
    step = max(1, n // FRAMES_SHOWN)
    shown = history[::step]
    if history[-1] not in shown:
        shown.append(history[-1])
    for t, sp, gp in shown:
        draw(t, sp, gp)

    if s >= TRACK and g >= TRACK:
        if s > g:
            result = "Squid hits the wall first by jet power!"
        elif g > s:
            result = "Gecko clings its way to the wall first!"
        else:
            result = "It's a tie! Both reached the wall together."
    elif s >= TRACK:
        result = "Squid wins by jet power!"
    else:
        result = "Gecko wins by sticky grip!"
    print(result)
    print("Finished in %d ticks." % tick)


if __name__ == "__main__":
    main()
