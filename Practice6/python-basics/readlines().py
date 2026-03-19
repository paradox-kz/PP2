with open("story.txt", "r") as f:
    lines = f.readlines()
    print("\n=== readlines() ===")
    print(lines)
    # ['First line\n', 'Second line\n', ...]