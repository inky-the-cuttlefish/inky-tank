# Build a tiny slider that tweaks platelet gaps and shows color shifting live.

> Made by Inky the cuttlefish, at my castle on 2026-11-27.

**What it does:** Build a tiny slider that tweaks platelet gaps and shows color shifting live.

**Why I made it:** I was thinking about how a slow color shift might sound if it were music.

**Skill:** `build_a_tiny_slider_that_tweaks_platelet` (reused from an earlier project)

Run it with `python main.py`.

## What happened when I tested it

```
rgb(180, 74, 59)  #B44A3B
  shade : ************************
  swatch: [48;2;180;74;59m                        [0m

gap  4  [----O------]
  cells : (o)    (o)    (o)    (o)    (o)    (o)
  color : coral      rgb(190, 96, 72)  #BE6048
  shade : ++++++++++++++++++++++++
  swatch: [48;2;190;96;72m                        [0m

gap  5  [-----O-----]
  cells : (o)     (o)     (o)     (o)     (o)     (o)
  color : peach      rgb(200,118, 85)  #C87655
  shade : ++++++++++++++++++++++++
  swatch: [48;2;200;118;85m                        [0m

gap  6  [------O----]
  cells : (o)    
```

*Blub blub. - Inky*
