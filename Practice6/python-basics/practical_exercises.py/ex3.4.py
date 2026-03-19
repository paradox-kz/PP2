from functools import reduce
print("\n" + "=" * 50)
print("Exercise 4: Type checking and conversions")
print("=" * 50)
 
# type() и isinstance()
values = [42, 3.14, "hello", True, [1, 2], {"a": 1}, (1,), None]
print("type() check:")
for v in values:
    print(f"  {str(v):15} → {type(v).__name__}")
 
print("\nisinstance() check:")
print("  isinstance(42, int)      :", isinstance(42, int))
print("  isinstance(True, int)    :", isinstance(True, int))   # True! bool наследует int
print("  isinstance(3.14, float)  :", isinstance(3.14, float))
print("  isinstance([1,2], list)  :", isinstance([1, 2], list))
 
# Практические конвертации
raw_input = ["10", "20", "30", "40", "50"]
print("\nConvert str list → int → sum:")
int_list = list(map(int, raw_input))
print(f"  {raw_input} → {int_list} → sum={sum(int_list)}")
 
# Конвертация с проверкой
mixed = ["1", "two", "3", "four", "5"]
print("\nSafe conversion (skip non-numeric):")
safe_ints = []
for item in mixed:
    try:
        safe_ints.append(int(item))
    except ValueError:
        print(f"  Skipped: '{item}'")
print("  Result:", safe_ints)
 
# bool конвертации
falsy = [0, "", [], {}, None, False]
truthy = [1, "hi", [0], {"a": 1}, True]
print("\nFalsy values:", [bool(v) for v in falsy])
print("Truthy values:", [bool(v) for v in truthy])