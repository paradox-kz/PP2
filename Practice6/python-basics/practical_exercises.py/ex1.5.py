import os
import shutil
print("\n" + "=" * 50)
print("Exercise 5: Delete files safely")
print("=" * 50)
 
files_to_delete = ["students_copy.txt", "students.txt"]
 
for filepath in files_to_delete:
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted: {filepath}")
    else:
        print(f"Skipped (not found): {filepath}")
 
# Удалить папку backup
shutil.rmtree("backup")
print("Deleted: backup/")
 
print("\nAll cleaned up.")