import math
import time

WIDTH = 64
HEIGHT = 15
FRAMES = 120
PLUCK_POS = 0.3
HARMONICS = 6


def amplitudes():
    amps = []
    for n in range(1, HARMONICS + 1):
        amps.append(math.sin(n * math.pi * PLUCK_POS) / (n * n))
    peak = max(abs(a) for a in amps) or 1.0
    return [a / peak for a in amps]


def displacement(x, t, amps):
    total = 0.0
    for i, a in enumerate(amps):
        n = i + 1
        decay = math.exp(-0.02 * n * t)
        total += a * decay * math.sin(n * math.pi * x) * math.cos(n * 0.6 * t)
    return total


def render(t, amps):
    grid = [[" "] * WIDTH for _ in range(HEIGHT)]
    mid = HEIGHT // 2
    for c in range(0, WIDTH, 2):
        grid[mid][c] = "-"
    for c in range(WIDTH):
        x = c / (WIDTH - 1)
        y = displacement(x, t, amps)
        row = mid - int(round(y * (mid - 1)))
        row = max(0, min(HEIGHT - 1, row))
        grid[row][c] = "#"
    for r in range(mid - 1, mid + 2):
        grid[r][0] = "|"
        grid[r][WIDTH - 1] = "|"
    return "\n".join("".join(r) for r in grid)


def main():
    amps = amplitudes()
    print("Plucking a virtual guitar string... hummmm")
    time.sleep(0.8)
    for f in range(FRAMES):
        t = f * 0.35
        print("\033[2J\033[H" + render(t, amps))
        print("\nframe %d/%d  (Ctrl-C to stop)" % (f + 1, FRAMES))
        time.sleep(0.05)
    print("\nThe string rests. *hmm*")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nstopped.")
