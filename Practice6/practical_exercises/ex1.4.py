import os
import shutil
print("\n" + "=" * 50)
print("Exercise 4: Copy and backup files")
print("=" * 50)
 
os.makedirs("backup", exist_ok=True)
 
# Простая копия
shutil.copy("students.txt", "students_copy.txt")
print("Copied → students_copy.txt")
 
# Копия в папку backup с датой
import datetime
today = datetime.date.today().strftime("%Y-%m-%d")
backup_name = f"backup/students_backup_{today}.txt"
shutil.copy2("students.txt", backup_name)
print(f"Backed up → {backup_name}")
 
print(f"Backup folder contents: {os.listdir('backup')}")