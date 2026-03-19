with open("story.txt", "r") as f:
    chunk = f.read(5)
    print("\n=== read(5) ===")
    print(repr(chunk))