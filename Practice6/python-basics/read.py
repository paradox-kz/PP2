with open("Sample.txt", "w") as f:
    f.write("Hello, Python!\nLine 2\nLine 3")
with open("Sample.txt", "r") as f:
    content = f.read()
    print("[r] Read:", content)