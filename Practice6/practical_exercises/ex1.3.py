import os
import shutil
print("\n" + "=" * 50)
print("Exercise 3: Append and verify")
print("=" * 50)
 
new_students = [
    "Frank, 24, Philosophy\n",
    "Grace, 22, Engineering\n",
]
 
with open("students.txt", "a") as f:
    f.writelines(new_students)
 
print("Appended 2 new students.")
print("Verified contents:")
 
with open("students.txt", "r") as f:
    lines = f.readlines()
 
print(f"  Total lines: {len(lines)}")
for line in lines:
    print(f"  {line.rstrip()}")