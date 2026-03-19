import os
import shutil
from pathlib import Path
 
BASE = "my_project"
print("\n" + "=" * 50)
print("Exercise 4: Move/copy files between directories")
print("=" * 50)
 
os.makedirs("my_project/archive", exist_ok=True)