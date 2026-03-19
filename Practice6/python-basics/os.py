import os
open("demo.txt", "w").close()
print("[os] exists:", os.path.exists("demo.txt"))   # True
print("[os] isfile:", os.path.isfile("demo.txt"))   # True
print("[os] isdir :", os.path.isdir("demo.txt"))    # False
 
# Разбор пути
path = "/home/user/projects/main.py"
print("[os] dirname :", os.path.dirname(path))    # /home/user/projects
print("[os] basename:", os.path.basename(path))   # main.py
print("[os] splitext:", os.path.splitext(path))   # ('/home/user/projects/main', '.py')
 
# Склейка пути (кроссплатформенно)
full = os.path.join("folder", "sub", "file.txt")
print("[os] join:", full)   # folder/sub/file.txt (на Linux/Mac)
 
# Переименование файла
os.rename("demo.txt", "renamed.txt")
print("[os] renamed demo.txt → renamed.txt")
 
# Размер файла
print("[os] size:", os.path.getsize("renamed.txt"), "bytes")