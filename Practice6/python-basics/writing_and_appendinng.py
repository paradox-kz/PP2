import os
 
# --- Запись текста ---
with open("log.txt", "w") as f:
    f.write("=== App Log ===\n")
    f.write("App started.\n")
print("[write] log.txt created.")
 
# --- Запись нескольких строк через writelines() ---
lines = ["Step 1: Init\n", "Step 2: Load\n", "Step 3: Run\n"]
with open("log.txt", "w") as f:
    f.writelines(lines)
print("[writelines] log.txt overwritten with steps.")
 
# --- Append: добавить новые строки, не удаляя старые ---
with open("log.txt", "a") as f:
    f.write("Step 4: Done\n")
    f.write("App finished.\n")
print("[append] Two lines added to log.txt.")
 
# --- Чтение результата ---
with open("log.txt", "r") as f:
    print("\n--- log.txt contents ---")
    print(f.read())
 
# --- Запись чисел и данных ---
data = [10, 20, 30, 40, 50]
with open("numbers.txt", "w") as f:
    for num in data:
        f.write(str(num) + "\n")
 
# Чтение обратно как числа
with open("numbers.txt", "r") as f:
    loaded = [int(line.strip()) for line in f]
print("Loaded numbers:", loaded)
 
# --- Запись в бинарном режиме (wb / ab) ---
with open("binary.bin", "wb") as f:
    f.write(b"\x00\xFF\x42\x13")
print("Binary file written.")
 
# Cleanup
for name in ["log.txt", "numbers.txt", "binary.bin"]:
    os.remove(name)