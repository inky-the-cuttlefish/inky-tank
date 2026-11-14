import random

random.seed(7)

CHAMBER_LIFT = 12       # grams of lift per gas-filled chamber
BASE_WEIGHT = 20        # grams of shell + body weight
WEIGHT_PER_CHAMBER = 3  # each new chamber adds a bit of shell weight


class Nautilus:
    def __init__(self, name):
        self.name = name
        self.chambers = []  # True = gas filled, False = flooded

    def grow_chamber(self):
        self.chambers.append(False)

    def pump_gas(self):
        for i, filled in enumerate(self.chambers):
            if not filled:
                self.chambers[i] = True
                return True
        return False

    def leak(self):
        gas = [i for i, f in enumerate(self.chambers) if f]
        if gas:
            self.chambers[random.choice(gas)] = False
            return True
        return False

    def lift(self):
        return sum(self.chambers) * CHAMBER_LIFT

    def weight(self):
        return BASE_WEIGHT + len(self.chambers) * WEIGHT_PER_CHAMBER

    def status(self):
        diff = self.lift() - self.weight()
        if diff > 5:
            return "FLOATING UP"
        if diff < -5:
            return "SINKING"
        return "HOVERING"

    def draw(self):
        shell = "".join("(O)" if f else "(.)" for f in self.chambers)
        return "<" + shell + ">="


def report(n, event):
    gas = sum(n.chambers)
    print("%-22s %s" % (event, n.draw()))
    print("   gas pockets: %d/%d | lift: %dg | weight: %dg | %s"
          % (gas, len(n.chambers), n.lift(), n.weight(), n.status()))


def main():
    n = Nautilus("Nelly")
    print("=== Chamber Counter for %s the Nautilus ===" % n.name)
    print("Legend: (O) = gas pocket, (.) = flooded chamber\n")
    for _ in range(4):
        n.grow_chamber()
        report(n, "Grew a new chamber")
        n.pump_gas()
        report(n, "Pumped gas")
    for _ in range(2):
        n.leak()
        report(n, "Gas leaked!")
    for _ in range(2):
        n.pump_gas()
        report(n, "Pumped gas")


main()
