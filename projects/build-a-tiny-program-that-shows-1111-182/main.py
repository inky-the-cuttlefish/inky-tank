import math

# Physics of a vibrating string: frequency is inversely proportional to length
# (tension and mass per unit length held constant).
# Reference: a 65 cm string plays A4 = 440 Hz.

REF_LENGTH_CM = 65.0
REF_FREQ_HZ = 440.0

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F",
              "F#", "G", "G#", "A", "A#", "B"]


def frequency(length_cm):
    return REF_FREQ_HZ * REF_LENGTH_CM / length_cm


def note_name(freq):
    # MIDI-style note number: A4 (440 Hz) is 69
    midi = round(69 + 12 * math.log2(freq / 440.0))
    name = NOTE_NAMES[midi % 12]
    octave = midi // 12 - 1
    return "%s%d" % (name, octave)


def main():
    print("=== How string length changes pitch ===")
    print("Shorter string -> faster vibration -> higher note!\n")
    print("%-10s %-12s %-6s" % ("Length", "Freq (Hz)", "Note"))
    print("-" * 30)

    lengths = [130, 115, 100, 90, 80, 72, 65, 58, 52, 46, 40, 36, 32.5]
    for length in lengths:
        f = frequency(length)
        print("%-10s %-12.1f %-6s" % ("%g cm" % length, f, note_name(f)))

    print("\nA tiny ASCII harp (longer strings = lower notes):\n")
    for length in lengths:
        f = frequency(length)
        bar = "~" * int(length / 3)
        print("%-4s |%s" % (note_name(f), bar))

    print("\nFun fact: halve the length and the pitch jumps up one octave.")
    half = REF_LENGTH_CM / 2
    print("%g cm = %.0f Hz (%s), %.1f cm = %.0f Hz (%s)" % (
        REF_LENGTH_CM, frequency(REF_LENGTH_CM),
        note_name(frequency(REF_LENGTH_CM)),
        half, frequency(half), note_name(frequency(half))))


if __name__ == "__main__":
    main()
