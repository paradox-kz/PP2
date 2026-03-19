import os
 
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
 
with open("new_file.txt", "x") as f:
    f.write("This file was just created!\n")
print("[x] New file created exclusively.")