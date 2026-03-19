import os
import shutil
print("\n" + "=" * 50)
print("Exercise 2: Read and print contents")
print("=" * 50)
 
with open("students.txt", "r") as f:
    contents = f.read()
 
print("Full file contents:")
print(contents)
 
# Читаем построчно
print("Line by line:")
with open("students.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        name, age, subject = line.strip().split(", ")
        print(f"  {i}. Name: {name}, Age: {age}, Subject: {subject}")