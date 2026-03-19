import os
import shutil
from pathlib import Path
 
BASE = "my_project"
print("\n" + "=" * 50)
print("Exercise 2: List files and folders")
print("=" * 50)
 
print(f"Top-level items in '{BASE}':", os.listdir(BASE))
 
print("\nFull tree (os.walk):")
for dirpath, dirnames, filenames in os.walk(BASE):
    level = dirpath.replace(BASE, "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(dirpath)}/")
    for fname in filenames:
        print(f"{indent}  {fname}")