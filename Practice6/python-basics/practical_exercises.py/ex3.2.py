from functools import reduce
print("\n" + "=" * 50)
print("Exercise 2: reduce() from functools")
print("=" * 50)
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Сумма
total = reduce(lambda a, b: a + b, numbers)
print("Sum      :", total)   # 55
 
# Произведение
product = reduce(lambda a, b: a * b, numbers)
print("Product  :", product) # 3628800
 
# Максимум без max()
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Max      :", maximum) # 10
 
# Склейка строк
words = ["Python", "is", "awesome"]
sentence = reduce(lambda a, b: a + " " + b, words)
print("Sentence :", sentence)
 
# Подсчёт суммы покупок с начальным значением (налог 100)
prices = [29.99, 49.99, 9.99, 15.00]
total_with_tax = reduce(lambda acc, p: acc + p, prices, 100)
print(f"Total with $100 base: ${total_with_tax:.2f}")