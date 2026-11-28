import random

random.seed(7)

# Toy model constants (rough, illustrative numbers)
GECKO_MASS_G = 50.0          # grams
GRAVITY = 9.81               # m/s^2
NUM_TOES = 5
SETAE_PER_TOE = 12           # tiny sample so output stays readable
BASE_FORCE_UN = 200.0        # micro-newtons per seta at perfect contact


def seta_grip(surface_roughness):
    """Return grip force (micro-newtons) of one seta.

    Contact quality is random; rougher surfaces lower the average contact.
    Van der Waals force falls off steeply with distance, modeled here
    as contact ** 3 (a simple stand-in for the 1/d^n behavior).
    """
    contact = random.uniform(0.3, 1.0) * (1.0 - surface_roughness)
    contact = max(contact, 0.0)
    return BASE_FORCE_UN * contact ** 3


def simulate(surface_name, roughness):
    print("=" * 50)
    print("Surface: %s (roughness %.2f)" % (surface_name, roughness))
    print("=" * 50)

    total_un = 0.0
    for toe in range(1, NUM_TOES + 1):
        toe_total = 0.0
        for _ in range(SETAE_PER_TOE):
            toe_total += seta_grip(roughness)
        total_un += toe_total
        per_hair = toe_total / SETAE_PER_TOE
        bar = "#" * int(per_hair / 6)
        print("Toe %d | avg %6.1f uN/hair | %s" % (toe, per_hair, bar))

    # Real geckos have millions of setae; scale the sample up.
    scale = 6000
    scaled_n = total_un * scale / 1e6   # newtons
    weight_n = GECKO_MASS_G / 1000.0 * GRAVITY
    print("-" * 50)
    print("Sampled setae : %d" % (NUM_TOES * SETAE_PER_TOE))
    print("Scaled grip   : %.2f N" % scaled_n)
    print("Gecko weight  : %.2f N" % weight_n)
    if scaled_n >= weight_n:
        ratio = scaled_n / weight_n
        print("Result: STUCK! Safety factor %.1fx. Hanging out." % ratio)
    else:
        print("Result: SPLAT! Not enough grip. Gecko slides down.")
    print()


def main():
    print("GECKO SETAE GRIP SIMULATOR")
    print("(van der Waals forces, one tiny hair at a time)\n")
    simulate("clean glass", 0.05)
    simulate("dusty wall", 0.45)
    simulate("wet sand", 0.85)


if __name__ == "__main__":
    main()