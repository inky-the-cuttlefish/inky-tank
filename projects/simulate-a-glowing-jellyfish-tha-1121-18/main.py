import math
import random
import time

# Glow levels from dim to bright, plain ASCII only
SHADES = " .:-=+*#%@"

def glow_char(level):
    """Pick a shading character for a brightness between 0.0 and 1.0."""
    level = max(0.0, min(1.0, level))
    return SHADES[int(level * (len(SHADES) - 1))]

def draw_jelly(brightness, frame):
    g = glow_char(brightness)
    g2 = glow_char(brightness * 0.7)
    sway = 1 if (frame // 2) % 2 == 0 else 0
    pad = " " * (6 + sway)
    lines = [
        pad + "  " + g * 7,
        pad + " " + g * 3 + g2 * 5 + g * 3,
        pad + g + g2 * 11 + g,
        pad + " " + g2 * 11,
        pad + "  " + "(" + "_" * 7 + ")",
    ]
    tentacle_chars = ["|", "/", "\\", "|"]
    for row in range(4):
        t = ""
        for col in range(6):
            t += tentacle_chars[(col + row + frame) % 4] + " "
        lines.append(pad + "  " + t)
    return "\n".join(lines)

def simulated_typing_speed(step):
    """Fake words-per-minute that rises and falls like bursts of typing."""
    base = 60 + 50 * math.sin(step / 6.0)
    return max(0, base + random.randint(-10, 10))

def main():
    random.seed()
    pulse = 0.0
    print("Glowing Jellyfish Simulator (typing speed is simulated)")
    print("=" * 50)
    for step in range(40):
        wpm = simulated_typing_speed(step)
        energy = min(1.0, wpm / 120.0)
        pulse = step / 2.0
        wave = (math.sin(pulse) + 1) / 2
        brightness = 0.15 + energy * 0.6 + wave * energy * 0.25
        bar = "#" * int(energy * 30)
        print("\nFrame %02d  WPM: %3d  [%-30s]" % (step, wpm, bar))
        print(draw_jelly(brightness, step))
        time.sleep(0.15)
    print("\nThe jellyfish drifts off into the deep, still glowing softly.")

if __name__ == "__main__":
    main()