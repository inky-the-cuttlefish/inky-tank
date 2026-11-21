import random

random.seed(7)

PATTERNS = {
    "stripes": "=-=-=-",
    "spots":   "o.o.O.",
    "waves":   "~^~^~^",
    "camo":    "#%#@%#",
    "plain":   ".....,",
}

WIDTH = 40
HEIGHT = 9


def make_pool():
    pool = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            r = random.random()
            if r < 0.08:
                row.append("*")  # pebble
            elif r < 0.12:
                row.append("'")  # bubble
            else:
                row.append("~")  # water
        pool.append(row)
    return pool


def draw_cuttlefish(pool, cx, cy, skin):
    body = [
        "  _____  ",
        " /{0}\\ ".format(skin),
        "( o  o  )",
        " \\_/\\/\\_/",
        "  ||||| ",
    ]
    for dy, line in enumerate(body):
        for dx, ch in enumerate(line):
            x = cx + dx
            y = cy + dy
            if 0 <= y < HEIGHT and 0 <= x < WIDTH and ch != " ":
                pool[y][x] = ch


def render(pool):
    border = "+" + "-" * WIDTH + "+"
    print(border)
    for row in pool:
        print("|" + "".join(row) + "|")
    print(border)


def main():
    names = list(PATTERNS.keys())
    print("Welcome to the Tide Pool! (simulated clicks)\n")
    for click in range(1, 6):
        name = names[(click - 1) % len(names)]
        skin = PATTERNS[name]
        pool = make_pool()
        cx = random.randint(2, WIDTH - 12)
        cy = random.randint(0, HEIGHT - 5)
        draw_cuttlefish(pool, cx, cy, skin)
        print("Click #%d -> skin pattern: %s" % (click, name))
        render(pool)
        print()
    print("The cuttlefish blinks and settles back into the sand. Bye!")


if __name__ == "__main__":
    main()