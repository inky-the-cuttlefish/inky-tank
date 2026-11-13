import random

random.seed(7)

# Two routes from NEST to FOOD: short (length 1) and long (length 3).
LENGTHS = [1.0, 3.0]
NAMES = ["short", "long"]
EVAPORATION = 0.1
ANTS = 20
ROUNDS = 15
GAIN = 0.1


def bar(x, scale=40):
    return "#" * int(round(x * scale))


def simulate():
    pher = [1.0, 1.0]
    print("=== Part 1: Ant simulation ===")
    print("Each ant picks a route with probability ~ pheromone.")
    print("Shorter route -> quicker trips -> more deposit (1/length).\n")
    for r in range(1, ROUNDS + 1):
        total = sum(pher)
        deposit = [0.0, 0.0]
        for _ in range(ANTS):
            i = 0 if random.random() < pher[0] / total else 1
            deposit[i] += 1.0 / LENGTHS[i]
        pher = [(1 - EVAPORATION) * pher[i] + GAIN * deposit[i]
                for i in range(2)]
        share = pher[0] / sum(pher)
        print("round %2d short %5.1f%% |%-40s|" % (r, share * 100, bar(share)))
    print()
    return share


def power_iteration():
    print("=== Part 2: The eigenvector view ===")
    print("On average, an ant picks route i with probability p_i = v_i / sum(v).")
    print("So the expected update is v' = M v with")
    print("  M[i][i] = (1 - evaporation) + GAIN * ANTS / (length_i * sum(v)).")
    print("Ignoring the sum(v) scaling, each route's weight is multiplied")
    print("by its own growth factor, so M is diagonal: the largest factor")
    print("wins. Repeated multiplication = power iteration.\n")
    # Use a fixed total of 1 for the normalized view (shares).
    m = [[(1 - EVAPORATION) + GAIN * ANTS / LENGTHS[0], 0.0],
         [0.0, (1 - EVAPORATION) + GAIN * ANTS / LENGTHS[1]]]
    print("Growth factors: short %.2f, long %.2f" % (m[0][0], m[1][1]))
    v = [0.5, 0.5]
    for step in range(1, ROUNDS + 1):
        v = [m[0][0] * v[0], m[1][1] * v[1]]
        s = sum(v)
        v = [v[0] / s, v[1] / s]
        print("step %2d short %5.1f%% |%-40s|" % (step, v[0] * 100, bar(v[0])))
    print()
    return v[0]


def main():
    sim = simulate()
    eig = power_iteration()
    print("Simulation ended at %.1f%% short; power iteration at %.1f%%."
          % (sim * 100, eig * 100))
    print("The dominant eigenvalue's eigenvector is [1, 0]: all weight on")
    print("the short route. Normalizing each step keeps only the direction.")


main()
