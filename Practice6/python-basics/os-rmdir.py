import os
try:
    os.rmdir("project")  # Не пустая → ошибка
except OSError as e:
    print("\n[rmdir] Can't remove non-empty dir:", e)