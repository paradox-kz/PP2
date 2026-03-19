import os
import shutil
from pathlib import Path
 
BASE = "my_project"
print("\n" + "=" * 50)
print("Exercise 3: Find files by extension")
print("=" * 50)
 
def find_by_extension(root, ext):
    result = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(ext):
                result.append(os.path.join(dirpath, fname))
    return result
 
py_files  = find_by_extension(BASE, ".py")
txt_files = find_by_extension(BASE, ".txt")
csv_files = find_by_extension(BASE, ".csv")
 
print(f".py  files ({len(py_files)}):")
for f in py_files:
    print(f"  {f}")
 
print(f".txt files ({len(txt_files)}):")
for f in txt_files:
    print(f"  {f}")
 
print(f".csv files ({len(csv_files)}):")
for f in csv_files:
    print(f"  {f}")
 
# pathlib glob — альтернативный способ
print("\nUsing pathlib glob (recursive .py):")
for p in Path(BASE).rglob("*.py"):
    print(f"  {p}")