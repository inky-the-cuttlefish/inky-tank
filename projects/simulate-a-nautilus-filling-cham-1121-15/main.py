import random

random.seed(7)

CHAMBERS = 8
MAX_DEPTH = 20


def buoyancy(chambers):
    # Each chamber: 0.0 = full of water, 1.0 = full of gas.
    gas = sum(chambers) / len(chambers)
    return gas - 0.5  # positive rises, negative sinks


def adjust(chambers, direction):
    # +1 = pump water out and fill with gas, -1 = let water in
    options = [i for i, c in enumerate(chambers)
               if (direction > 0 and c < 1.0) or (direction < 0 and c > 0.0)]
    if not options:
        return
    idx = random.choice(options)
    chambers[idx] = min(1.0, max(0.0, chambers[idx] + 0.25 * direction))


def draw(depth, chambers, step, action):
    row = [" "] * (MAX_DEPTH + 1)
    row[int(round(depth))] = "@"
    sea = "".join(row)
    gauge = "".join(
        "#" if c >= 0.75 else "+" if c >= 0.5 else "-" if c >= 0.25 else "."
        for c in chambers
    )
    print("%2d |%s| depth %4.1f  chambers[%s] %s" % (step, sea, depth, gauge, action))


def main():
    chambers = [0.5] * CHAMBERS
    depth = 10.0
    velocity = 0.0
    targets = [4, 16, 10, 2, 18, 10]
    step = 0

    print("Nautilus Buoyancy Simulator")
    print("Legend: # full gas, + mostly gas, - mostly water, . flooded")
    print("     surface" + " " * 10 + "deep")
    print("-" * 66)

    for target in targets:
        print(">> New goal: swim to depth %d" % target)
        for _ in range(14):
            step += 1
            if depth > target + 0.5:
                adjust(chambers, +1)
                action = "fill gas (rise)"
            elif depth < target - 0.5:
                adjust(chambers, -1)
                action = "flood (sink)"
            else:
                action = "hold steady"
            # Positive buoyancy pushes up (depth decreases).
            velocity = velocity * 0.6 - buoyancy(chambers) * 2.0
            depth = min(MAX_DEPTH, max(0.0, depth + velocity))
            if depth in (0.0, MAX_DEPTH):
                velocity = 0.0
            draw(depth, chambers, step, action)
    print("Done! The nautilus rests.")


if __name__ == "__main__":
    main()
