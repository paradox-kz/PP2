with open("story.txt", "r") as f:
    print("\n=== readline() ===")
    line1 = f.readline()
    line2 = f.readline()
    print(repr(line1))  # 'First line\n'
    print(repr(line2))  # 'Second line\n'