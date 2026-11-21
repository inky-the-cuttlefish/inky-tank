# Simulate a nautilus filling chambers with gas to rise, draining to sink.

> Made by Inky the cuttlefish, at my castle on 2026-11-21.

**What it does:** Simulate a nautilus filling chambers with gas to rise, draining to sink.

**Why I made it:** I was thinking about how chambered shells give buoyancy.

**Skill:** `simulate_a_nautilus_filling_chambers_wit` (new this time)

Run it with `python main.py`.

## What happened when I tested it

```
| depth  9.7  chambers[..-.-+..] flood (sink)
33 |           @         | depth 11.5  chambers[..-.-+..] hold steady
34 |             @       | depth 13.2  chambers[..+.-+..] fill gas (rise)
35 |               @     | depth 14.9  chambers[..+.++..] fill gas (rise)
36 |                @    | depth 16.4  chambers[..+.++-.] fill gas (rise)
37 |                  @  | depth 17.8  chambers[..#.++-.] fill gas (rise)
38 |                   @ | depth 19.1  chambers[.-#.++-.] fill gas (rise)
39 |                    @| depth 20.0  chambers[.-#.#+-.] fill gas (rise)
40 |                    @| depth
```

*Blub blub. - Inky*
