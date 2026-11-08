# Fossil sorter: groups fossils by geological age based on their date (Ma = million years ago)

FOSSILS = [
    ("Opabinia", 508),
    ("Anomalocaris", 508),
    ("Hallucigenia", 508),
    ("Wiwaxia", 508),
    ("Marrella", 508),
    ("Pikaia", 508),
    ("Trilobite (Olenellus)", 515),
    ("Dunkleosteus", 370),
    ("Tiktaalik", 375),
    ("Eurypterid", 430),
    ("Dimetrodon", 290),
    ("Coelophysis", 210),
    ("Tyrannosaurus", 68),
    ("Archaeopteryx", 150),
    ("Woolly Mammoth", 0.01),
    ("Megalodon", 15),
]

# (name, oldest Ma, youngest Ma), checked in order, contiguous so nothing falls through
AGES = [
    ("Quaternary", 2.6, 0),
    ("Neogene", 23, 2.6),
    ("Paleogene", 66, 23),
    ("Cretaceous", 145, 66),
    ("Jurassic", 201, 145),
    ("Triassic", 252, 201),
    ("Permian", 299, 252),
    ("Carboniferous", 359, 299),
    ("Devonian", 419, 359),
    ("Silurian", 444, 419),
    ("Ordovician", 485, 444),
    ("Cambrian", 539, 485),
]

BURGESS = "Burgess Shale (Cambrian, ~508 Ma)"


def classify(ma):
    # Burgess Shale window: roughly 505-510 Ma, mid-Cambrian
    if 505 <= ma <= 510:
        return BURGESS
    for name, old, new in AGES:
        if new <= ma <= old:
            return name
    return "Other / in-between age"


def main():
    groups = {}
    for name, ma in FOSSILS:
        groups.setdefault(classify(ma), []).append((name, ma))

    print("=" * 50)
    print("   FOSSIL SORTING MACHINE  (beep boop, crunch)")
    print("=" * 50)

    # Burgess Shale first, then the rest from youngest to oldest
    def sort_key(g):
        members = groups[g]
        return (g != BURGESS, min(ma for _, ma in members))

    for group in sorted(groups, key=sort_key):
        print(f"\n[ {group} ]")
        for name, ma in sorted(groups[group], key=lambda f: f[1]):
            bar = "#" * max(1, round(ma / 25))
            print(f"  {name:<24}{ma:>8g} Ma  {bar}")

    print(f"\nSorted {len(FOSSILS)} fossils into {len(groups)} groups. Crunch!")


if __name__ == "__main__":
    main()
