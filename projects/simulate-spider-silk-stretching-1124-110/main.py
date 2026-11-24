import time
import sys

WIDTH = 60
STRENGTH_LIMIT = 1.40
STIFFNESS = 0.35
DAMPING = 0.12


def render_strand(length, anchor_left=2):
    length = max(1, min(WIDTH - anchor_left - 2, int(round(length))))
    body = "".join("~" if i % 2 == 0 else "-" for i in range(length))
    line = "|" + " " * (anchor_left - 1) + body + "O"
    return line.ljust(WIDTH + 2) + "|"


def tension_bar(ratio):
    pct = max(0.0, min(1.0, abs(ratio - 1.0) / (STRENGTH_LIMIT - 1.0)))
    filled = int(pct * 20)
    return "[" + "#" * filled + "." * (20 - filled) + "] " + str(int(pct * 100)).rjust(3) + "%"


def draw(pos, rest, label):
    print(render_strand(pos), tension_bar(pos / rest), label.ljust(8))


def main():
    rest_length = 20.0
    pull_target = rest_length * 1.35
    pos = rest_length
    vel = 0.0
    print("=== SPIDER SILK STRETCH TEST ===")
    print("Silk can stretch ~35% and still spring back!")
    print()

    for _ in range(12):
        pos += (pull_target - pos) * 0.35
        draw(pos, rest_length, "PULLING")
        time.sleep(0.05)

    print("-" * (WIDTH + 3))
    print("Release! Watch the web bounce...")
    print("-" * (WIDTH + 3))

    snapped = False
    for _ in range(40):
        force = -STIFFNESS * (pos - rest_length)
        vel = (vel + force) * (1.0 - DAMPING)
        pos += vel
        if pos / rest_length > STRENGTH_LIMIT:
            snapped = True
            break
        draw(pos, rest_length, "RECOIL")
        time.sleep(0.05)

    print("-" * (WIDTH + 3))
    if snapped:
        print("SNAP! The silk broke.")
    else:
        print("The silk settled back to rest. Tough little thread!")


if __name__ == "__main__":
    main()
