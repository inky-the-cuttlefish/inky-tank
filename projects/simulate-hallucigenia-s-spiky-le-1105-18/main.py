import random
import time

WIDTH = 60
FRAMES = 40
random.seed(7)

SAND = "".join(random.choice(".,'` ") for _ in range(WIDTH + 20))
WATER = "".join(random.choice("~-") for _ in range(WIDTH + 20))

def build_frame(pos, step):
    body = "o" + "=" * 9 + "~"
    tent = " " + "".join("w" if i % 2 == step else "v" for i in range(9)) + "  "
    # one row of legs: planted legs reach the floor, lifted ones are short
    legs = " " + "".join(
        ("/" if i % 2 == 0 else "\\") if i % 2 == step else "'"
        for i in range(10)
    )
    pad = " " * pos
    floor = list(SAND)
    # footprints trail behind the animal
    for p in range(1, pos + 1, 2):
        floor[p] = "u"
    for i in range(10):
        if i % 2 == step:
            idx = pos + 1 + i
            if idx < len(floor):
                floor[idx] = "V"
    rows = [
        pad + tent,
        pad + body,
        pad + legs,
        "".join(floor)[:WIDTH + 20],
        WATER,
    ]
    return "\n".join(rows)

def main():
    for f in range(FRAMES):
        pos = f % (WIDTH - 12)
        step = (f // 2) % 2
        print("\033[2J\033[H" + build_frame(pos, step), flush=True)
        time.sleep(0.12)
    print("Hallucigenia wanders off into the deep. *blub*")

if __name__ == "__main__":
    main()
