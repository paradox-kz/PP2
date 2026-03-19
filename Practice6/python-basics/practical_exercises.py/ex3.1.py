from functools import reduce
 
# ── Exercise 1: map() and filter() on lists ──────────────────
print("=" * 50)
print("Exercise 1: map() and filter()")
print("=" * 50)
 
temperatures_c = [0, 20, 37, 100, -10, 25, 36.6]
 
# map: конвертировать Celsius → Fahrenheit
to_fahrenheit = list(map(lambda c: round(c * 9/5 + 32, 1), temperatures_c))
print("Celsius    :", temperatures_c)
print("Fahrenheit :", to_fahrenheit)
 
# map: все имена в верхний регистр
names = ["alice", "bob", "charlie", "diana"]
upper_names = list(map(str.upper, names))
print("\nOriginal :", names)
print("Uppercased:", upper_names)
 
# filter: только тёплые температуры (> 20°C)
warm = list(filter(lambda c: c > 20, temperatures_c))
print("\nWarm temps (>20°C):", warm)
 
# filter: имена длиннее 4 букв
long_names = list(filter(lambda n: len(n) > 4, names))
print("Long names (>4)   :", long_names)
 
# filter + map вместе: тёплые → сразу в Fahrenheit
warm_f = list(map(
    lambda c: round(c * 9/5 + 32, 1),
    filter(lambda c: c > 20, temperatures_c)
))
print("Warm in Fahrenheit:", warm_f)