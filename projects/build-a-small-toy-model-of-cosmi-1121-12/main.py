import math
import random

N_LAYERS = 100
DT = 10.0            # true kyr per layer
MEAN_FLUX = 1.0
BASE_SED_RATE = 5.0


def run(wobble, seed=42):
    rng = random.Random(seed)  # same noise sequence for every wobble level
    true_age = 0.0
    est_age = 0.0
    max_err = 0.0
    for i in range(N_LAYERS):
        sed = BASE_SED_RATE * (1 + 0.3 * math.sin(2 * math.pi * i / 23.0))
        th = sed * DT / 10.0
        cycle = math.sin(2 * math.pi * i * DT / 100.0)
        noise = rng.gauss(0, 0.5)
        flux = max(0.1, MEAN_FLUX * (1 + wobble * (cycle + 0.5 * noise)))
        conc = flux * DT / th            # He-3 per cm in this layer
        # Inferred: assume constant flux, so duration = conc * th / MEAN_FLUX
        est_dt = conc * th / MEAN_FLUX
        true_age += DT
        est_age += est_dt
        max_err = max(max_err, abs(est_age - true_age))
    final_err = est_age - true_age
    return max_err, final_err, 100 * final_err / true_age


print("Cosmic-dust He-3 age model distortion (toy)")
print(f"Total true duration: {N_LAYERS * DT:.0f} kyr")
print("-" * 52)
print(f"{'flux wobble':<14}{'max err kyr':<14}{'final err':<12}{'final %':<10}")
for w in (0.0, 0.1, 0.25, 0.5, 0.8):
    m, f, p = run(w)
    print(f"{w:<14.2f}{m:<14.1f}{f:<12.1f}{p:<10.2f}")
