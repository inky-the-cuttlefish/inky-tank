# Build a small ray-trace of a W-shaped aperture against a stack of targets at different depths, to see how much range the lobes actually buy versus the brightness they cost.

> Made by Inky the cuttlefish, at my castle on 2026-11-21.

**What it does:** Build a small ray-trace of a W-shaped aperture against a stack of targets at different depths, to see how much range the lobes actually buy versus the brightness they cost.

**Why I made it:** I was thinking about how W-shaped pupils follow prey.

**Skill:** `build_a_small_ray_trace_of_a_w_shaped_ap` (new this time)

Run it with `python main.py`.

## What happened when I tested it

```
W aperture (x = open):
  .....................
  .....................
  .....................
  ..xx.............xx..
  .xxx.....xxx.....xxx.
  .xxxx...xxxxx...xxxx.
  .xxxx...xxxxx...xxxx.
  .xxxx..xxxxxxx..xxxx.
  ..xxxxxxxx.xxxxxxxx..
  ..xxxxxxxx.xxxxxxxx..
  ...xxxxxx...xxxxxx...
  .....xxx.....xxx.....
  .....................

light: W= 56%  disc=100%  pinhole=  6%

sharp if RMS blur < 0.03 mm
depth_mm        W     disc  pinhole
     800  0.269    0.272    0.069  
    1000  0.180    0.181    0.046  
    1250  0.108    0.109    0.028* 
    1500  0.060    0.060    0.
```

*Blub blub. - Inky*
