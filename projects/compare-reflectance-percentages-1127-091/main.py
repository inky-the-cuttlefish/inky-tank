# Compare reflectance of white patterns in fish and squid using an ASCII bar chart.
# NOTE: The numbers below are illustrative, made-up values for fun, not real measurements.

data = [
    ("Fish: guanine scales",      88),
    ("Fish: silvery belly",       82),
    ("Fish: pale cheek patch",    64),
    ("Fish: white fin spot",      71),
    ("Squid: leucophores",        92),
    ("Squid: iridophores",        78),
    ("Squid: white arm stripe",   69),
    ("Squid: mantle spot",        75),
]

BAR_WIDTH = 40  # characters for 100%


def make_bar(pct):
    filled = int(round(pct / 100 * BAR_WIDTH))
    return "#" * filled + "." * (BAR_WIDTH - filled)


def average(group):
    vals = [v for name, v in data if name.startswith(group)]
    return sum(vals) / len(vals)


def main():
    label_width = max(len(name) for name, _ in data)
    line_width = label_width + BAR_WIDTH + 12
    print("=" * line_width)
    print("WHITE PATTERN REFLECTANCE: FISH vs SQUID")
    print("(illustrative made-up numbers)")
    print("=" * line_width)

    for name, pct in data:
        print("%-*s |%s| %3d%%" % (label_width, name, make_bar(pct), pct))

    print("-" * line_width)
    fish_avg = average("Fish")
    squid_avg = average("Squid")
    print("%-*s |%s| %5.1f%%" % (label_width, "Fish average", make_bar(fish_avg), fish_avg))
    print("%-*s |%s| %5.1f%%" % (label_width, "Squid average", make_bar(squid_avg), squid_avg))
    print()

    if squid_avg > fish_avg:
        winner = "Squid"
        diff = squid_avg - fish_avg
    elif fish_avg > squid_avg:
        winner = "Fish"
        diff = fish_avg - squid_avg
    else:
        winner = None
        diff = 0

    if winner:
        print("%s win the shine contest by %.1f points!" % (winner, diff))
    else:
        print("It's a perfect tie. Equally shiny!")


if __name__ == "__main__":
    main()
