import math

def squid_step(state):
    # Squid: mantle contracts, jets water, then coasts while drag slows it.
    mass = 1.0
    v = state["v"]
    t = state["t"]
    phase = t % 10  # 10-tick jet cycle
    if phase < 2:
        thrust = 3.2   # jet pulse
    elif phase < 5:
        thrust = 0.0   # coasting
    else:
        thrust = -0.2  # refill mantle (slight stall)
    drag = 0.45 * v * abs(v)
    a = (thrust - drag) / mass
    v = max(0.0, v + a * 0.5)
    state["v"] = v
    state["x"] += v * 0.5
    state["t"] += 1

def gecko_step(state):
    # Gecko: toes alternate stick and peel; steady, slip-prone climb.
    t = state["t"]
    stick = 0.5 + 0.5 * math.sin(t * 0.9)
    pull = 0.55 * stick
    slip = 0.05 if stick < 0.2 else 0.0
    state["x"] += max(0.0, pull - slip)
    state["t"] += 1

def draw(name, x, goal, width=40):
    pos = int(min(x, goal) / goal * width)
    track = ["."] * (width + 1)
    track[pos] = name[0]
    return "%-7s|%s|" % (name, "".join(track))

def main():
    goal = 20.0
    squid = {"x": 0.0, "v": 0.0, "t": 0}
    gecko = {"x": 0.0, "t": 0}
    finish = {}
    for tick in range(1, 81):
        squid_step(squid)
        gecko_step(gecko)
        for name, s in (("Squid", squid), ("Gecko", gecko)):
            if name not in finish and s["x"] >= goal:
                finish[name] = tick
        if tick % 10 == 0:
            print("tick %2d" % tick)
            print(draw("Squid", squid["x"], goal))
            print(draw("Gecko", gecko["x"], goal))
            print()
        if len(finish) == 2:
            break
    if not finish:
        print("Nobody reached the goal.")
    else:
        for name, tick in sorted(finish.items(), key=lambda kv: kv[1]):
            print("%s finished at tick %d" % (name, tick))
        winner = min(finish, key=finish.get)
        print("Winner: %s!" % winner)

if __name__ == "__main__":
    main()
