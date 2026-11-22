import math
import time

WIDTH = 41
CENTER = WIDTH // 2

# A W pupil, two rows tall, centered on column 0
W_TOP = {-6: "\\", -5: " ", -4: "/", -3: "\\", -2: " ", -1: "/",
         1: "\\", 2: " ", 3: "/", 4: "\\", 6: "/"}
W_BOT = {-5: "_", -4: " ", -2: "_", 0: "_", 2: "_", 5: "_"}


def prey_position(t):
    # Prey drifts back and forth with a little wobble
    x = CENTER + 15 * math.sin(t * 0.25) + 3 * math.sin(t * 0.9)
    return int(round(max(1, min(WIDTH - 2, x))))


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def draw_frame(t, prey_x, eye_offset):
    scene = [" "] * WIDTH
    scene[prey_x] = "o"

    top = [" "] * WIDTH
    bot = [" "] * WIDTH
    for dx, ch in W_TOP.items():
        x = CENTER + dx + eye_offset
        if 0 <= x < WIDTH:
            top[x] = ch
    for dx, ch in W_BOT.items():
        x = CENTER + dx + eye_offset
        if 0 <= x < WIDTH:
            bot[x] = ch

    marker = [" "] * WIDTH
    marker[CENTER] = "|"

    lines = [
        "t=%02d  prey offset: %+d  eye offset: %+d"
        % (t, prey_x - CENTER, eye_offset),
        "water : " + "".join(scene),
        "pupil : " + "".join(top),
        "        " + "".join(bot),
        "center: " + "".join(marker),
        "-" * (WIDTH + 8),
    ]
    return "\n".join(lines)


def main(frames=40, delay=0.15):
    eye_offset = 0
    for t in range(frames):
        prey_x = prey_position(t)
        # Eye steps toward the prey, at most 2 columns per frame
        error = (prey_x - CENTER) - eye_offset
        eye_offset += clamp(error, -2, 2)
        eye_offset = clamp(eye_offset, -12, 12)
        print(draw_frame(t, prey_x, eye_offset))
        time.sleep(delay)


if __name__ == "__main__":
    main()
