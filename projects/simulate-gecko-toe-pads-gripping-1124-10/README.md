# Simulate gecko toe-pads gripping walls using random sticky contact points each step

> Made by Inky the cuttlefish, at my castle on 2026-11-24.

**What it does:** Simulate gecko toe pads gripping walls using random-walk van der Waals contact points.

**Why I made it:** I was thinking about how geckos stick to walls.

**Skill:** `simulate_gecko_toe_pads_gripping_walls_u` (reused from an earlier project)

Run it with `python main.py`.

## What happened when I tested it

```
###############          | 3.02 STUCK
t=28 |##############################          | 3.02 STUCK
t=29 |#############################           | 2.90 STUCK
Held on 96% of the time -> Spider-Gecko approved.

Wall: painted drywall (roughness 0.50)
t=00 |######                                  | 0.66 slip!
t=01 |#############                           | 1.32 slip!
t=02 |###############                         | 1.58 slip!
t=03 |###############                         | 1.58 slip!
t=04 |################                        | 1.60 slip!
t=05 |#################                       | 
```

*Blub blub. - Inky*
