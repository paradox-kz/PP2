import os
import shutil
from pathlib import Path
 
BASE = "my_project"
print("=" * 50)
print("Exercise 1: Create nested directories")
print("=" * 50)
 
dirs = [
    "my_project/src/utils",
    "my_project/src/models",
    "my_project/tests",
    "my_project/data/raw",
    "my_project/data/processed",
    "my_project/docs",
]
 
for d in dirs:
    os.makedirs(d, exist_ok=True)
 
print("Created structure:")
for d in dirs:
    print(f"  {d}/")
 
# Создадим тестовые файлы в разных папках
sample_files = {
    "my_project/src/main.py":           "# main entry point\n",
    "my_project/src/utils/helpers.py":  "# helper functions\n",
    "my_project/src/models/user.py":    "# User model\n",
    "my_project/tests/test_main.py":    "# tests\n",
    "my_project/data/raw/data.csv":     "name,age\nAlice,30\nBob,25\n",
    "my_project/data/raw/notes.txt":    "raw notes here\n",
    "my_project/data/processed/clean.csv": "name,age\nAlice,30\n",
    "my_project/docs/README.md":        "# Project Docs\n",
    "my_project/docs/notes.txt":        "Some notes\n",
}
 
for path, content in sample_files.items():
    with open(path, "w") as f:
        f.write(content)
 
print("Sample files created.")