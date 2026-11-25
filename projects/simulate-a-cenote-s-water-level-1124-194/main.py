import math
import random

random.seed(7)

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

MAX_DEPTH = 30.0      # meters from cenote floor to rim
level = 14.0          # starting water level in meters
EVAPORATION = 0.9     # meters lost per month (warm climate)
SEEPAGE = 0.04        # fraction of water lost to underground flow


def rainfall(month):
    """Seasonal rain: peaks around Aug-Sep, low in Feb-Mar, plus noise."""
    # month index 0=Jan; sine peaks at month 7.5 (between Aug and Sep)
    seasonal = math.sin((month - 4.5) / 12.0 * 2 * math.pi)
    base = 1.6 + 1.5 * seasonal          # meters of water-equivalent inflow
    storm = random.choice([0, 0, 0, 0.5, 1.2])
    return max(0.0, base + storm + random.uniform(-0.3, 0.3))


print("=" * 60)
print("  CENOTE WATER LEVEL SIMULATOR  (24 months)")
print("=" * 60)
print("  Rim at %.0f m. Each # is about 1 meter of water.\n" % MAX_DEPTH)

lowest = (MAX_DEPTH, "")
highest = (0.0, "")

for step in range(24):
    m = step % 12
    year = step // 12 + 1
    rain = rainfall(m)
    level = level + rain - EVAPORATION - level * SEEPAGE
    level = max(1.0, min(MAX_DEPTH, level))

    label = "%s Y%d" % (MONTHS[m], year)
    bar = "#" * int(round(level))
    pad = " " * (int(MAX_DEPTH) - int(round(level)))
    rain_icon = "~" * int(round(rain))
    print("%-7s|%s%s| %5.1fm  rain:%s" % (label, bar, pad, level, rain_icon))

    if level < lowest[0]:
        lowest = (level, label)
    if level > highest[0]:
        highest = (level, label)

print()
print("=" * 60)
print("  Lowest:  %.1f m in %s" % lowest)
print("  Highest: %.1f m in %s" % highest)
print("=" * 60)
