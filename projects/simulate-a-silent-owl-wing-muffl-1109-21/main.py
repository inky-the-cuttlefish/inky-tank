import math
import random

random.seed(7)

WIDTH = 40
SAMPLES = 24


def make_noise(n):
    """Jagged turbulence: a hum plus random sharp spikes."""
    out = []
    for i in range(n):
        base = math.sin(i / 2.0) * 3
        spike = random.choice([0, 0, 0, 6, -6, 9, -9]) * random.random()
        out.append(base + spike + random.uniform(-2, 2))
    return out


def owl_comb(signal, teeth=5):
    """Each 'feather tooth' averages neighbors, breaking up big waves."""
    half = teeth // 2
    result = []
    for i in range(len(signal)):
        lo = max(0, i - half)
        hi = min(len(signal), i + half + 1)
        window = signal[lo:hi]
        result.append(sum(window) / len(window))
    return result


def rms(signal):
    return math.sqrt(sum(x * x for x in signal) / len(signal))


def peak(signal):
    return max(abs(x) for x in signal)


def bar(value, scale):
    length = int(abs(value) / scale * WIDTH)
    return "#" * length


def show(title, signal, scale):
    print(title)
    print("-" * (WIDTH + 12))
    for i, v in enumerate(signal):
        print("%2d %+6.2f %s" % (i, v, bar(v, scale)))
    print()


def main():
    print("=== SILENT OWL WING SIMULATOR ===")
    print("Wing fringe: ,,,/\\/\\/\\/\\,,, (comb of feather teeth)")
    print()

    noisy = make_noise(SAMPLES)
    quiet = owl_comb(noisy, teeth=5)
    quieter = owl_comb(quiet, teeth=3)

    scale = peak(noisy)

    show("RAW AIR TURBULENCE (loud!)", noisy, scale)
    show("AFTER OWL COMB (hushed)", quiet, scale)
    show("AFTER FINE FRINGE (silent)", quieter, scale)

    print("LOUDNESS REPORT")
    print("-" * (WIDTH + 12))
    for name, sig in (("raw", noisy), ("comb", quiet), ("fringe", quieter)):
        print("%-7s rms %5.2f  peak %5.2f" % (name, rms(sig), peak(sig)))
    cut = 100 * (1 - rms(quieter) / rms(noisy))
    print()
    print("Noise cut by %.0f%%. Hoo goes there? Nobody heard." % cut)


if __name__ == "__main__":
    main()
