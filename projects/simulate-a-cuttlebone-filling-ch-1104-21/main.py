import random

random.seed(7)

CHAMBERS = 10
CUTTLEFISH_MASS = 100.0   # arbitrary units
WATER_DENSITY = 1.0

def make_bone():
    # Each chamber holds a fraction of gas (0.0 = liquid, 1.0 = gas)
    return [0.5] * CHAMBERS

def buoyancy(bone):
    # More gas -> more lift. Body weight pulls down.
    lift = sum(bone) * 20.0 * WATER_DENSITY
    return lift - CUTTLEFISH_MASS * 0.9 * WATER_DENSITY

def draw_bone(bone):
    rows = []
    for i, g in enumerate(bone):
        filled = int(round(g * 10))
        bar = "#" * filled + "." * (10 - filled)
        rows.append("  chamber %2d [%s] %3d%% gas" % (i + 1, bar, int(round(g * 100))))
    return "\n".join(rows)

def depth_gauge(net):
    # Net > 0 floats up (left), net < 0 sinks (right)
    pos = max(0, min(20, int(round(10 - net / 4))))
    line = ["~"] * 21
    line[pos] = "C"
    return "surface |" + "".join(line) + "| seabed"

def adjust(bone):
    net = buoyancy(bone)
    if abs(net) < 3.0:
        return "holding steady"
    if net < 0:
        idx = min(range(CHAMBERS), key=lambda i: bone[i])
        bone[idx] = min(1.0, bone[idx] + 0.2)
        return "pumping liquid out of chamber %d (rising)" % (idx + 1)
    idx = max(range(CHAMBERS), key=lambda i: bone[i])
    bone[idx] = max(0.0, bone[idx] - 0.2)
    return "flooding chamber %d with liquid (sinking)" % (idx + 1)

def main():
    bone = make_bone()
    for step in range(1, 16):
        if step % 5 == 0:
            i = random.randrange(CHAMBERS)
            bone[i] = max(0.0, min(1.0, bone[i] + random.choice([-0.3, 0.3])))
            print("  (a current nudges chamber %d)" % (i + 1))
        net = buoyancy(bone)
        action = adjust(bone)
        print("\nStep %d: net force %.2f -> %s" % (step, net, action))
        print(depth_gauge(buoyancy(bone)))
        print(draw_bone(bone))

if __name__ == "__main__":
    main()
