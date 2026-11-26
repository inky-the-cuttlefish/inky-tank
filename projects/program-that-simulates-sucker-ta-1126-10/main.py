import random

random.seed(42)

OBJECTS = {
    "strawberry": {"sweet": 8, "chewy": 3, "safe": True},
    "gummy bear": {"sweet": 9, "chewy": 9, "safe": True},
    "lollipop": {"sweet": 10, "chewy": 1, "safe": True},
    "brick": {"sweet": 0, "chewy": 0, "safe": False},
    "sock": {"sweet": 0, "chewy": 6, "safe": False},
    "pickle": {"sweet": 2, "chewy": 4, "safe": True},
    "pencil": {"sweet": 0, "chewy": 2, "safe": False},
    "marshmallow": {"sweet": 9, "chewy": 8, "safe": True},
    "rock": {"sweet": 0, "chewy": 0, "safe": False},
    "lemon": {"sweet": 1, "chewy": 3, "safe": True},
}

REACTIONS = {
    "yum": ["Mmm, sugary bliss!", "Sucker-approved!", "Gimme more!"],
    "meh": ["It's... fine.", "Not a sucker's first pick.", "Edible, but sad."],
    "yuck": ["Blegh! Spit it out!", "Sucker says NO.", "Absolutely not."],
}


def taste_score(props):
    if not props["safe"]:
        return 0
    base = props["sweet"] * 8 + props["chewy"] * 2
    wobble = random.randint(-5, 5)
    return max(0, min(100, base + wobble))


def verdict(score):
    if score >= 60:
        return "EDIBLE", "yum"
    if score >= 20:
        return "EDIBLE (barely)", "meh"
    return "NOT EDIBLE", "yuck"


def bar(score):
    filled = score // 10
    return "[" + "#" * filled + "." * (10 - filled) + "]"


def main():
    print("=" * 46)
    print("      THE SUCKER TASTE SIMULATOR 3000")
    print("=" * 46)
    edible = 0
    for name, props in OBJECTS.items():
        score = taste_score(props)
        label, mood = verdict(score)
        if mood != "yuck":
            edible += 1
        print(f"{name:<12} {bar(score)} {score:>3}  {label}")
        print(f"{'':<12} -> {random.choice(REACTIONS[mood])}")
    print("=" * 46)
    print(f"{edible} of {len(OBJECTS)} objects passed the sucker test.")


if __name__ == "__main__":
    main()
