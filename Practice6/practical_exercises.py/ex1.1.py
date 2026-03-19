import os
import shutil
print("=" * 50)
print("Exercise 1: Create and write file")
print("=" * 50)
 
with open("students.txt", "w") as f:
    f.write("Alice, 20, Math\n")
    f.write("Bob, 22, Physics\n")
    f.write("Charlie, 21, Chemistry\n")
    f.write("Diana, 23, Biology\n")
    f.write("Eve, 20, Computer Science\n")
 
print("File 'students.txt' created with 5 records.")