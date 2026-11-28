import colorsys
import sys
import time

# Hue (degrees) -> chord, walking around the circle of fifths
CHORDS = [
    ("C major",  ["C4", "E4", "G4", "B4"]),
    ("G major",  ["G3", "B3", "D4", "F#4"]),
    ("D major",  ["D4", "F#4", "A4", "C#5"]),
    ("A minor",  ["A3", "C4", "E4", "G4"]),
    ("E minor",  ["E3", "G3", "B3", "D4"]),
    ("B minor",  ["B3", "D4", "F#4", "A4"]),
    ("F# minor", ["F#3", "A3", "C#4", "E4"]),
    ("Db major", ["Db4", "F4", "Ab4", "C5"]),
    ("Ab major", ["Ab3", "C4", "Eb4", "G4"]),
    ("Eb major", ["Eb4", "G4", "Bb4", "D5"]),
    ("Bb major", ["Bb3", "D4", "F4", "A4"]),
    ("F major",  ["F3", "A3", "C4", "E4"]),
]

NAMES = ["red", "orange", "yellow", "lime", "green", "teal",
         "cyan", "azure", "blue", "violet", "magenta", "rose"]


def bar(hue, width=36):
    pos = int(hue / 360 * (width - 1))
    cells = ["-"] * width
    cells[pos] = "#"
    return "[" + "".join(cells) + "]"


def main():
    # Optional: pass seconds-per-chord as an argument (60 for real time)
    delay = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    print("=== Hue Piano Clock: one chord per minute ===")
    print()
    for minute in range(12):
        hue = minute * 30
        r, g, b = colorsys.hsv_to_rgb(hue / 360, 0.6, 0.9)
        rgb = "(%3d,%3d,%3d)" % (int(r * 255), int(g * 255), int(b * 255))
        name, notes = CHORDS[minute]
        print("Minute %02d  hue %3d deg  %-8s %s" % (minute, hue, NAMES[minute], rgb))
        print("  " + bar(hue))
        print("  Chord: %-9s -> %s" % (name, " ".join(notes)))
        print("  (soft, slow, let it ring...)")
        print()
        sys.stdout.flush()
        if delay:
            time.sleep(delay)
    print("The hue wheel has turned a full circle. Twelve chords, one hour.")


if __name__ == "__main__":
    main()
