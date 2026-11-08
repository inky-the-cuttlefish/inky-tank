import math
import random

random.seed(42)

PKB = 8.60
D11B_SW = 39.61
ALPHA = 1.0272
EPS = (ALPHA - 1) * 1000.0


def true_ph(t):
    """Fake 'real' pH history; t is millions of years ago."""
    dip = 0.25 * math.exp(-((t - 55) ** 2) / 50.0)  # PETM-ish dip
    return 8.05 - dip - 0.0015 * (t / 10.0) ** 2 + 0.05 * math.sin(t / 7.0)


def forward(ph):
    """pH -> d11B of borate."""
    f = 1.0 / (1.0 + 10 ** (PKB - ph))  # fraction as borate
    return D11B_SW - (1 - f) * EPS


def invert(d_b4):
    """d11B of borate -> pH (standard paleo-pH equation)."""
    num = D11B_SW - d_b4
    den = D11B_SW - ALPHA * d_b4 - EPS
    return PKB - math.log10(-num / den)


def main():
    lo, hi, width = 7.4, 8.3, 40
    print("ANCIENT SEAWATER pH FROM BORON ISOTOPES (simulated)")
    print(f"{'Ma':>4} {'d11B':>6} {'pH':>5}  chart ({lo} .. {hi})")
    for t in range(100, -1, -5):
        d = forward(true_ph(t)) + random.gauss(0, 0.15)  # measurement noise
        ph = invert(d)
        pos = int((ph - lo) / (hi - lo) * (width - 1))
        pos = max(0, min(width - 1, pos))
        row = [" "] * width
        row[pos] = "*"
        print(f"{t:4d} {d:6.2f} {ph:5.2f}  |{''.join(row)}|")


main()
