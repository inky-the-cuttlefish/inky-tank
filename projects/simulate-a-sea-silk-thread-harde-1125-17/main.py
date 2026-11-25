import random

random.seed(7)

WIDTH = 40
STRANDS = 5
FRAMES = 14


def render(positions, hardness):
    row = [" "] * WIDTH
    chars = "~-=#"
    level = min(len(chars) - 1, int(hardness * len(chars)))
    ch = chars[level]
    for p in positions:
        row[int(p)] = ch
    return "".join(row)


def step(positions, frame, braid_phase):
    center = WIDTH / 2
    pull = 0.15 + frame * 0.04
    new = []
    for i, p in enumerate(positions):
        drift = random.uniform(-1.5, 1.5) * (1 - frame / FRAMES)
        p += (center - p) * pull + drift
        if braid_phase:
            # weave side to side around the center, narrowing over time
            width = max(0.3, (STRANDS - i) * 0.3 * (1 - frame / FRAMES))
            offset = (1 if (frame + i) % 2 == 0 else -1) * width
            p = center + (p - center) * 0.5 + offset
        p = max(0, min(WIDTH - 1, p))
        new.append(p)
    return new


def main():
    positions = [random.uniform(2, WIDTH - 3) for _ in range(STRANDS)]
    print("SEA SILK: from drifting strands to hardened thread")
    print("+" + "-" * WIDTH + "+")
    for frame in range(FRAMES):
        braid_phase = frame > FRAMES // 3
        positions = step(positions, frame, braid_phase)
        hardness = frame / (FRAMES - 1)
        label = "drifting"
        if braid_phase:
            label = "braiding"
        if hardness > 0.75:
            label = "hardening"
        if frame == FRAMES - 1:
            label = "HARD THREAD"
        print("|" + render(positions, hardness) + "| " + label)
    print("+" + "-" * WIDTH + "+")


if __name__ == "__main__":
    main()
