import random

random.seed(42)

GRAVITY = 9.81
WALL_HEIGHT = 10
MAX_TURNS = 40


class Gecko:
    def __init__(self, name, mass_g, toe_pads, cleanliness):
        self.name = name
        self.mass = mass_g / 1000.0
        self.toe_pads = toe_pads
        self.clean = cleanliness
        self.height = 0.0
        self.slips = 0
        self.finished_turn = None

    def grip_force(self, glass_wetness):
        # More pads and clean feet help; a wet pane hurts.
        base = self.toe_pads * 0.12 * self.clean
        return base * (1.0 - glass_wetness)

    def step(self, angle_deg, wetness, turn):
        if self.finished_turn is not None:
            return
        pull = self.mass * GRAVITY * (angle_deg / 90.0)
        grip = self.grip_force(wetness) * random.uniform(0.6, 1.2)
        if grip >= pull:
            self.height += random.uniform(0.4, 1.0)
            if self.height >= WALL_HEIGHT:
                self.height = float(WALL_HEIGHT)
                self.finished_turn = turn
        else:
            self.slips += 1
            self.height = max(0.0, self.height - 0.5)


def draw(geckos):
    for g in geckos:
        pos = int(min(g.height, WALL_HEIGHT))
        track = ["."] * (WALL_HEIGHT + 1)
        track[pos] = "G"
        print("%-10s |%s| %4.1f m  slips:%d" % (
            g.name, "".join(track), g.height, g.slips))


def main():
    geckos = [
        Gecko("Tokay", 150, 20, 0.95),
        Gecko("LeafTail", 60, 14, 0.90),
        Gecko("Dusty", 90, 18, 0.50),
        Gecko("Chubby", 220, 16, 0.85),
    ]
    angle = 85
    wetness = 0.15
    print("=== GECKO GLASS CLIMB ===")
    print("Pane angle: %d deg, wetness: %d%%" % (angle, wetness * 100))
    for turn in range(1, MAX_TURNS + 1):
        for g in geckos:
            g.step(angle, wetness, turn)
        if turn % 5 == 0:
            print("\n--- turn %d ---" % turn)
            draw(geckos)
        if all(g.finished_turn is not None for g in geckos):
            break
    print("\n=== RESULTS ===")
    ranked = sorted(geckos, key=lambda g: (
        g.finished_turn if g.finished_turn is not None else 999, -g.height))
    for i, g in enumerate(ranked, 1):
        status = ("reached top on turn %d" % g.finished_turn
                  if g.finished_turn else "stuck at %.1f m" % g.height)
        print("%d. %-10s %s (slips: %d)" % (i, g.name, status, g.slips))


if __name__ == "__main__":
    main()
