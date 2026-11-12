import random
import math

random.seed(7)

WIDTH = 48
DEPTHS = [5, 15, 30, 50]


def make_scene(depth):
    """Build a row of water pixels with a dim hidden prey blob."""
    ambient = max(0.05, 1.0 - depth / 60.0)
    row = []
    prey_start = random.randint(8, WIDTH - 14)
    prey_len = random.randint(5, 8)
    for x in range(WIDTH):
        glare = ambient * (0.7 + 0.3 * math.sin(x / 3.0))
        noise = random.uniform(-0.05, 0.05)
        val = glare + noise
        if prey_start <= x < prey_start + prey_len:
            val += 0.04 * ambient + 0.02  # very faint contrast
        row.append(max(0.0, val))
    return row, prey_start, prey_len


def w_pupil_filter(row):
    """Two-lobed W pupil: subtract smooth glare, boost local contrast."""
    out = []
    for i in range(len(row)):
        lo = max(0, i - 4)
        hi = min(len(row), i + 5)
        local = sum(row[lo:hi]) / (hi - lo)
        out.append((row[i] - local) * 8.0 + 0.5)
    return out


def round_pupil(row):
    """Plain pupil: just passes the light through."""
    return list(row)


def to_ascii(row):
    chars = " .:-=+*#%@"
    lo, hi = min(row), max(row)
    span = (hi - lo) or 1.0
    s = ""
    for v in row:
        idx = int((v - lo) / span * (len(chars) - 1))
        s += chars[idx]
    return s


def contrast(row, start, length):
    """Prey mean vs background mean, relative to the image's full range."""
    inside = row[start:start + length]
    outside = row[:start] + row[start + length:]
    mi = sum(inside) / len(inside)
    mo = sum(outside) / len(outside)
    span = (max(row) - min(row)) or 1.0
    return abs(mi - mo) / span


def verdict(c):
    if c >= 0.25:
        return "easy to spot"
    if c >= 0.12:
        return "maybe..."
    return "hard to tell"


def main():
    print("=== W-PUPIL PREY SPOTTER ===")
    print("Prey position marked with ^ below each image\n")
    for depth in DEPTHS:
        row, start, length = make_scene(depth)
        rnd = round_pupil(row)
        w = w_pupil_filter(row)
        marker = " " * start + "^" * length
        print(f"Depth {depth} m")
        print("round: |" + to_ascii(rnd) + "|")
        print("W-eye: |" + to_ascii(w) + "|")
        print("prey : |" + marker.ljust(WIDTH) + "|")
        cr = contrast(rnd, start, length)
        cw = contrast(w, start, length)
        print(f"contrast round={cr:.3f} ({verdict(cr)})  "
              f"W={cw:.3f} ({verdict(cw)})\n")


if __name__ == "__main__":
    main()
