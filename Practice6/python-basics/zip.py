from functools import reduce
 
nums = [4, 7, 1, 9, 3, 6, 2, 8, 5]
words = ["banana", "apple", "cherry", "date"]
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
grades = ["A", "B", "A"]
 
print("\nzip:")
for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score} ({grade})")