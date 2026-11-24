import random

random.seed(42)

SETAE = 200
STEPS = 30
FORCE_PER_SETA = 0.02
GECKO_WEIGHT = 2.0


def make_pad(n):
    return [{"x": random.random(), "y": random.random(), "on": False}
            for _ in range(n)]


def bump(x, y, roughness):
    # Deterministic bumpy wall: rough walls have more bad spots.
    return ((int(x * 10) * 7 + int(y * 10) * 13) % 10) / 10.0 < roughness


def step(pad, roughness):
    for s in pad:
        s["x"] = min(1.0, max(0.0, s["x"] + random.uniform(-0.1, 0.1)))
        s["y"] = min(1.0, max(0.0, s["y"] + random.uniform(-0.1, 0.1)))
        bad = bump(s["x"], s["y"], roughness)
        if s["on"]:
            p_peel = 0.10 + roughness * 0.2 + (0.2 if bad else 0.0)
            if random.random() < p_peel:
                s["on"] = False
        else:
            p_stick = 0.45 - roughness * 0.3 - (0.15 if bad else 0.0)
            if random.random() < p_stick:
                s["on"] = True


def grip(pad):
    return sum(FORCE_PER_SETA for s in pad if s["on"])


def run(name, roughness):
    pad = make_pad(SETAE)
    print("Wall: %s (roughness %.2f)" % (name, roughness))
    holds = 0
    for t in range(STEPS):
        step(pad, roughness)
        g = grip(pad)
        ok = g >= GECKO_WEIGHT
        holds += ok
        bar = "#" * int(g * 10)
        print("t=%02d |%-40s| %.2f %s" % (t, bar[:40], g, "STUCK" if ok else "slip!"))
    pct = 100 * holds // STEPS
    verdict = "Spider-Gecko approved." if pct >= 80 else "Gecko needs a better wall."
    print("Held on %d%% of the time -> %s\n" % (pct, verdict))


if __name__ == "__main__":
    run("smooth glass", 0.05)
    run("painted drywall", 0.50)
    run("rough brick", 0.90)
