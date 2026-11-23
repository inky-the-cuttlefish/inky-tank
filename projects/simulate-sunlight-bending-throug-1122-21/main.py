import math

W, H = 70, 28          # floor grid size
DEPTH = 6.0            # water depth (in grid units)
N_WATER = 1.33         # refractive index of water
RAYS = 4               # sub-rays per surface cell, for smoother light
t = 1.7                # time of the "snapshot"

def height(x, y):
    """Wave surface height from a few summed sine waves."""
    return (0.30 * math.sin(0.35 * x + 1.3 * t)
            + 0.25 * math.sin(0.28 * y - 0.9 * t + 1.0)
            + 0.20 * math.sin(0.20 * (x + y) + 0.6 * t)
            + 0.15 * math.sin(0.50 * x - 0.4 * y + 1.7 * t))

def slope(x, y):
    """Numerical gradient of the surface."""
    e = 0.01
    dx = (height(x + e, y) - height(x - e, y)) / (2 * e)
    dy = (height(x, y + e) - height(x, y - e)) / (2 * e)
    return dx, dy

floor = [[0.0] * W for _ in range(H)]

for j in range(H):
    for i in range(W):
        for a in range(RAYS):
            for b in range(RAYS):
                x = i + (a + 0.5) / RAYS
                y = j + (b + 0.5) / RAYS
                sx, sy = slope(x, y)
                # Surface tilt; sunlight comes straight down.
                g = math.hypot(sx, sy)
                if g == 0:
                    fx, fy = x, y
                else:
                    cos_i = 1.0 / math.sqrt(1 + g * g)
                    sin_i = math.sqrt(max(0.0, 1 - cos_i * cos_i))
                    sin_r = sin_i / N_WATER
                    # Angle between refracted ray and vertical
                    theta_i = math.asin(sin_i)
                    theta_r = math.asin(sin_r)
                    bend = theta_i - theta_r  # deviation from straight down
                    # Horizontal shift of the ray over the water depth.
                    # The ray bends toward the downhill direction of the slope.
                    # Shift measured from straight down: tan(theta_r) gives
                    # offset relative to the normal; the normal itself tilts.
                    shift = DEPTH * math.tan(bend)
                    fx = x + shift * (sx / g)
                    fy = y + shift * (sy / g)
                ix, iy = int(math.floor(fx)), int(math.floor(fy))
                if 0 <= ix < W and 0 <= iy < H:
                    floor[iy][ix] += 1.0

peak = max(max(r) for r in floor)
ramp = " .:-=+*#%@"
print("Sunlight caustics on the tank floor")
print("+" + "-" * W + "+")
for row in floor:
    line = ""
    for v in row:
        k = int((v / (peak * 0.6)) * (len(ramp) - 1))
        line += ramp[min(k, len(ramp) - 1)]
    print("|" + line + "|")
print("+" + "-" * W + "+")
