from functools import reduce
 
nums = [4, 7, 1, 9, 3, 6, 2, 8, 5]
words = ["banana", "apple", "cherry", "date"]
print("\nenumerate:")
for i, word in enumerate(words, start=1):
    print(f"  {i}. {word}")