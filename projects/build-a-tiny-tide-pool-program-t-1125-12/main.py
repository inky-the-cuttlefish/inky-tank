import random

random.seed(7)

WIDTH, HEIGHT = 30, 8
NUM_BARNACLES = 40
WAVES = 5


def make_rock():
    # '~' = wet rock, '.' = dry rock (higher up the shore)
    rock = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            row.append("~" if y >= HEIGHT // 3 else ".")
        rock.append(row)
    return rock


def drop_barnacles(rock):
    barnacles = {}
    attempts = 0
    while len(barnacles) < NUM_BARNACLES and attempts < 1000:
        attempts += 1
        x = random.randrange(WIDTH)
        y = random.randrange(HEIGHT)
        if (x, y) in barnacles:
            continue
        wet = rock[y][x] == "~"
        # wet rock gives a better grip; dry rock is risky
        base = random.uniform(0.4, 0.9)
        grip = base if wet else base * 0.5
        barnacles[(x, y)] = grip
    return barnacles


def draw(rock, barnacles, title):
    print(title)
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if (x, y) in barnacles:
                g = barnacles[(x, y)]
                line += "O" if g > 0.6 else "o"
            else:
                line += rock[y][x]
        print(line)
    print()


def run_waves(barnacles):
    for wave in range(1, WAVES + 1):
        force = random.uniform(0.3, 0.8) + wave * 0.03
        lost = []
        for pos, grip in barnacles.items():
            push = force * random.random() + 0.1
            if grip < push:
                lost.append(pos)
        for pos in lost:
            del barnacles[pos]
        print("Wave %d (force %.2f): %d barnacles washed away, %d left"
              % (wave, force, len(lost), len(barnacles)))
    print()


def main():
    print("=== TINY TIDE POOL ===")
    print("Legend: . dry rock  ~ wet rock  o weak grip  O strong grip")
    print()
    rock = make_rock()
    barnacles = drop_barnacles(rock)
    start = len(barnacles)
    draw(rock, barnacles, "Freshly settled barnacles:")
    run_waves(barnacles)
    draw(rock, barnacles, "After the waves:")
    pct = 100 * len(barnacles) // max(start, 1)
    print("%d of %d barnacles held on (%d%%)." % (len(barnacles), start, pct))


if __name__ == "__main__":
    main()
