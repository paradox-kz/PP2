import os
print("\n[walk] Full tree of project/:")
for dirpath, dirnames, filenames in os.walk("project"):
    indent = "  " * dirpath.count(os.sep)
    print(f"{indent}{dirpath}/")
    for fname in filenames:
        print(f"{indent}  {fname}")