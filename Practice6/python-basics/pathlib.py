import os
import shutil
from pathlib import Path
p = Path("renamed.txt")
print("\n[pathlib] path   :", p)
print("[pathlib] name   :", p.name)       # renamed.txt
print("[pathlib] stem   :", p.stem)       # renamed
print("[pathlib] suffix :", p.suffix)     # .txt
print("[pathlib] parent :", p.parent)     # .
print("[pathlib] exists :", p.exists())   # True
 
# Чтение / запись через pathlib
p.write_text("Written via pathlib!\n")
print("[pathlib] read   :", p.read_text().strip())
 
# Построение пути через /
new_path = Path("folder") / "sub" / "file.txt"
print("[pathlib] joined :", new_path)
 
# Glob (поиск файлов)
cwd = Path(".")
txt_files = list(cwd.glob("*.txt"))
print("[pathlib] .txt files:", [f.name for f in txt_files])
 
# Cleanup
for name in ["renamed.txt", "copy.txt", "moved.txt"]:
    if os.path.exists(name):
        os.remove(name)