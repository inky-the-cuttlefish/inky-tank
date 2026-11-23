import random

SHIMMERS = {
    "pink":   "p",
    "mint":   "m",
    "lilac":  "l",
    "gold":   "g",
    "sky":    "s",
    "peach":  "a",
    "silver": "o",
}

ROWS = 12
TILES_PER_ROW = 8
TILE_WIDTH = 6
MORTAR_V = "|"
SPARKLE = 0.18


def pick():
    return random.choice(list(SHIMMERS.values()))


def make_tile(width):
    color = pick()
    return "".join("*" if random.random() < SPARKLE else color
                   for _ in range(width))


def make_row(offset):
    parts = []
    if offset:
        parts.append(make_tile(TILE_WIDTH // 2))
    count = TILES_PER_ROW - 1 if offset else TILES_PER_ROW
    for _ in range(count):
        parts.append(make_tile(TILE_WIDTH))
    if offset:
        parts.append(make_tile(TILE_WIDTH // 2))
    return MORTAR_V.join(parts)


def make_mortar(width):
    return "".join("~" if random.random() < 0.15 else "-"
                   for _ in range(width))


def main():
    random.seed()
    print("=== NACRE: Mother-of-Pearl Brick Wall ===")
    print()
    for r in range(ROWS):
        row = make_row(r % 2)
        print(row)
        if r < ROWS - 1:
            print(make_mortar(len(row)))


if __name__ == "__main__":
    main()
