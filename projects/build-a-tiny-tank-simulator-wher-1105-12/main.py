import random

random.seed(7)

TANK_HEIGHT = 12
WIDTH = 30


class Cuttlefish:
    def __init__(self):
        self.depth = 6.0      # 0 = surface, TANK_HEIGHT-1 = bottom
        self.gas = 50         # percent gas in cuttlebone chambers
        self.velocity = 0.0

    def adjust(self, target_depth):
        # More gas = more buoyant = rises. Less gas = sinks.
        # Predict where we will be soon, to avoid overshooting.
        predicted = self.depth + self.velocity * 3
        if predicted < target_depth - 0.5:
            self.gas = max(0, self.gas - 6)
        elif predicted > target_depth + 0.5:
            self.gas = min(100, self.gas + 6)
        else:
            if self.gas > 50:
                self.gas -= 3
            elif self.gas < 50:
                self.gas += 3

    def step(self):
        buoyancy = (self.gas - 50) / 50.0
        self.velocity += -buoyancy * 0.25
        self.velocity *= 0.7  # water drag
        self.depth += self.velocity
        if self.depth <= 0 or self.depth >= TANK_HEIGHT - 1:
            self.velocity = 0.0
        self.depth = min(TANK_HEIGHT - 2, max(0, self.depth))


def draw(fish, tick, target):
    rows = []
    for y in range(TANK_HEIGHT):
        if y == TANK_HEIGHT - 1:
            row = list("~" * WIDTH)
        else:
            row = [" "] * WIDTH
            if y == int(round(target)):
                row[0] = "-"
                row[1] = ">"
        rows.append(row)
    y = int(round(fish.depth))
    sprite = "<(o.o)<" if fish.velocity <= 0 else "<(-.-)<"
    x = 8 + (tick % 10)
    for i, ch in enumerate(sprite):
        if x + i < WIDTH:
            rows[y][x + i] = ch
    if y > 0 and random.random() < 0.4 and x + 7 < WIDTH:
        rows[y - 1][x + 7] = random.choice("o.")
    lines = ["+" + "-" * WIDTH + "+"]
    lines += ["|" + "".join(r) + "|" for r in rows]
    lines.append("+" + "-" * WIDTH + "+")
    return "\n".join(lines)


def main():
    fish = Cuttlefish()
    target = 9
    for tick in range(60):
        if tick % 20 == 0 and tick:
            target = random.randint(1, TANK_HEIGHT - 3)
            print(f">>> New goal: depth {target}")
        fish.adjust(target)
        fish.step()
        bar = "#" * (fish.gas // 5)
        print(draw(fish, tick, target))
        print(f"Gas  [{bar:<20}] {fish.gas:3d}%")
        print(f"Depth {fish.depth:.1f}  Target {target}  Speed {fish.velocity:.2f}\n")


if __name__ == "__main__":
    main()
