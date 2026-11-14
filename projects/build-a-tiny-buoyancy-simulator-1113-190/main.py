# Cuttlebone buoyancy simulator (stdlib only, ASCII output)

CHAMBERS = 8
BODY_DENSITY = 1.060
SEAWATER = 1.025
GAS_EFFECT = 0.004
MAX_DEPTH = 30.0


class Cuttlebone:
    def __init__(self):
        self.liquid = [1.0] * CHAMBERS  # 1.0 = liquid, 0.0 = gas

    def pump(self, idx, amount):
        """Positive drains liquid (adds gas), negative fills."""
        self.liquid[idx] = min(1.0, max(0.0, self.liquid[idx] - amount))

    def density(self):
        gas = sum(1.0 - x for x in self.liquid)
        return BODY_DENSITY - GAS_EFFECT * gas * 2.5

    def bar(self):
        out = ""
        for x in self.liquid:
            if x > 0.66:
                out += "#"
            elif x > 0.33:
                out += "+"
            elif x > 0.0:
                out += "-"
            else:
                out += "."
        return "[" + out + "]"


def main():
    cb = Cuttlebone()
    depth = 10.0
    velocity = 0.0
    plan = [
        ("drain", 4, 0.5), ("drain", 6, 0.5), ("hold", 0, 0),
        ("drain", 7, 0.5), ("hold", 0, 0), ("hold", 0, 0),
        ("fill", 3, 0.5), ("fill", 5, 0.5), ("hold", 0, 0),
        ("fill", 6, 0.5), ("hold", 0, 0), ("hold", 0, 0),
    ]
    print("CUTTLEBONE BUOYANCY SIMULATOR")
    print("# = liquid  + = mixed  - = mostly gas  . = gas")
    print("")
    step = 0
    for action, n, amt in plan:
        step += 1
        if action == "drain":
            cb.pump(n, amt)
        elif action == "fill":
            cb.pump(n, -amt)
        d = cb.density()
        # net force: denser than water sinks, lighter rises; drag damps speed
        velocity = velocity * 0.5 + (d - SEAWATER) * 100
        depth = min(MAX_DEPTH, max(0.0, depth + velocity))
        if depth <= 0.0:
            velocity = 0.0
        if abs(d - SEAWATER) < 0.003:
            state = "neutral"
        elif d > SEAWATER:
            state = "sinking"
        else:
            state = "rising"
        pos = int(depth / MAX_DEPTH * 40)
        print("t=%02d %-5s %s dens=%.4f %s" % (step, action, cb.bar(), d, state))
        print("     |" + " " * pos + "<(o)>  depth %.1f m" % depth)
    print("")
    print("Final density %.4f vs seawater %.3f" % (cb.density(), SEAWATER))


if __name__ == "__main__":
    main()
