import os
 
# --- Зачем with? ---
# БЕЗ with: нужно вручную закрывать файл, и при ошибке он может не закрыться.
f = open("manual.txt", "w")
try:
    f.write("Manual management is risky.\n")
finally:
    f.close()  # Нужно не забыть!
print("[manual] File closed manually.")
 
# С with: файл закрывается АВТОМАТИЧЕСКИ, даже при исключении.
with open("context.txt", "w") as f:
    f.write("Context manager rocks!\n")
# f уже закрыт здесь
print("[with] File closed automatically. f.closed =", f.closed)
 
# --- with при чтении ---
with open("context.txt", "r") as f:
    data = f.read()
    print("[read]", data.strip())
 
# --- Несколько файлов в одном with ---
with open("input.txt", "w") as src, open("output.txt", "w") as dst:
    src.write("Source data\n")
    dst.write("Destination data\n")
print("[multi-with] Two files written at once.")
 
# --- with ловит ошибки корректно ---
try:
    with open("context.txt", "r") as f:
        content = f.read()
        raise ValueError("Simulated error inside with block")
except ValueError as e:
    print("[error] Caught:", e)
    print("[error] File still closed:", f.closed)  # True!
 
# --- Свой контекст-менеджер через __enter__ / __exit__ ---
class Timer:
    import time
 
    def __enter__(self):
        import time
        self._start = time.time()
        print("[Timer] Started.")
        return self  # возвращается как `as` переменная
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self._start
        print(f"[Timer] Elapsed: {elapsed:.4f}s")
        return False  # не подавляем исключения
 
with Timer() as t:
    total = sum(range(1_000_000))
print("Sum:", total)
 
# Cleanup
for name in ["manual.txt", "context.txt", "input.txt", "output.txt"]:
    if os.path.exists(name):
        os.remove(name)