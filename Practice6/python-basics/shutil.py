import shutil
import os
shutil.copy("renamed.txt", "copy.txt")
print("[shutil] copy made: copy.txt")
 
# Копирование с метаданными (права, время)
shutil.copy2("renamed.txt", "copy2.txt")
print("[shutil] copy2 made: copy2.txt")
 
# Копирование папки (нужна непустая папка)
os.makedirs("src_dir", exist_ok=True)
with open("src_dir/hello.txt", "w") as f:
    f.write("hi")
shutil.copytree("src_dir", "dst_dir")
print("[shutil] copytree: src_dir → dst_dir")
 
# Удаление папки рекурсивно
shutil.rmtree("src_dir")
shutil.rmtree("dst_dir")
print("[shutil] rmtree: folders removed")
 
# Перемещение файла
shutil.move("copy2.txt", "moved.txt")
print("[shutil] moved copy2.txt → moved.txt")