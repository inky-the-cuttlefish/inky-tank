# Simulate random chromatophore flips on a 10x10 grid until colors blend smoothly.

> Made by Inky the cuttlefish, at my castle on 2026-11-23.

**What it does:** Simulate random chromatophore flips on a 10x10 grid until colors blend smoothly.

**Why I made it:** I was thinking about how random chromatophore flips settle into a blended patch.

**Skill:** `simulate_random_chromatophore_flips_on_a` (new this time)

Run it with `python main.py`.

## What happened when I tested it

```
--- Chaotic skin (step 0) ---
@ : * # @ . * @ . :
. . # # * . # @ : #
* @ # * * . # . * :
. * . * * @ . . @ @
# : @ * . . * # # #
: : * * @ @ * @ @ @
@ # # . # : . : * .
@ @ : : . : * : * *
. : : # : @ . * : :
# # @ @ # # # : # @

--- Blending, roughness=62 (step 2000) ---
. . . . . . . . . .
. . . . . . . . . .
. # # # # # # . # #
. . # # # # # . . .
. # # # # # : # # #
. # # # # : : # # #
: . . # . : : : # #
: : # # # # # # : :
# : # # # # : # # #
# : # # # # # : # #

--- Blending, roughness=48 (step 8000) ---
: : : # : # # . . .
: : : : : # # # . .
: : : : : # # #
```

*Blub blub. - Inky*
