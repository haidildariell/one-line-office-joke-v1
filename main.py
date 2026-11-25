JOKE = "HR's wellness program gave us a meditation app, a standing desk, and a poster of a beach, so now we burn out upright, hydrated, and staring at a paper ocean."


def get_joke():
    return JOKE


def validate(text):
    if not 1 <= len(text) <= 200:
        raise ValueError("joke must be 1-200 characters")
    if "\n" in text:
        raise ValueError("joke must be a single line")
    return text


def main():
    import os

    text = validate(get_joke())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
