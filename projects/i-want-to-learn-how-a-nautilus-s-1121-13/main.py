import random

NAUTILUS = {
    "type": "External coiled shell (calcium carbonate, aragonite)",
    "chambers": "Many gas-filled chambers joined by a tube (siphuncle)",
    "buoyancy": "Adjusts gas/liquid in chambers slowly",
    "location": "Outside the body; animal lives in the last chamber",
    "depth": "Roughly 100-700 m, often deeper by day",
}

CUTTLEBONE = {
    "type": "Internal, porous, chalky plate (aragonite)",
    "chambers": "Thin, laminated layers with tiny pillars and gas spaces",
    "buoyancy": "Pumps fluid in and out for fine control",
    "location": "Inside the mantle, along the back",
    "depth": "Usually shallow shelf waters, up to ~200 m",
}

RELATIVES = [
    ("Cuttlefish", "Internal cuttlebone, W-shaped pupils, master of camouflage."),
    ("Squid", "Internal flexible gladius (pen), fast jet-propelled swimmers."),
    ("Octopus", "No shell at all, eight arms, very flexible and clever."),
    ("Nautilus", "Only living shelled cephalopod with many tentacles, no suckers."),
    ("Spirula", "Deep-sea squid with a small coiled internal shell, glowing tail."),
    ("Vampire squid", "Deep-sea dweller with a tiny internal shell and cloak-like webbing."),
]

ART = r"""
   Nautilus            Cuttlefish
     ,--.               ______
   /  __ \\            /      \\=--
  | (@  ) |          ( o    o  )===
   \\ \\__/ /           \\______/ ===
    '-..-'              ||||||
"""

def compare():
    print("=== SHELL vs CUTTLEBONE ===")
    for key in NAUTILUS:
        print(f"\n[{key.upper()}]")
        print(f"  Nautilus   : {NAUTILUS[key]}")
        print(f"  Cuttlebone : {CUTTLEBONE[key]}")

def album():
    print("\n=== LIVING CEPHALOPOD RELATIVES ===")
    for name, fact in RELATIVES:
        print(f"* {name:<14} - {fact}")

def fun_fact():
    facts = [
        "Nautilus has about 90 tentacles called cirri, without suckers.",
        "Cuttlebone is sold for pet birds as a calcium supplement.",
        "Nautiluses have changed little in hundreds of millions of years.",
        "Cuttlefish have three hearts and blue-green blood.",
        "Nautilus shell chambers follow a spiral close to logarithmic.",
    ]
    print("\n=== RANDOM FUN FACT ===")
    print(random.choice(facts))

def main():
    print(ART)
    compare()
    album()
    fun_fact()
    print("\nTip: Both structures help with buoyancy, but one is worn")
    print("outside like a house and the other hides inside like a float.")

if __name__ == "__main__":
    main()