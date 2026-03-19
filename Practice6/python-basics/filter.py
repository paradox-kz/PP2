from functools import reduce
 
nums = [4, 7, 1, 9, 3, 6, 2, 8, 5]
words = ["banana", "apple", "cherry", "date"]
evens = list(filter(lambda x: x % 2 == 0, nums))
print("\nfilter evens :", evens)
 
long_words = list(filter(lambda w: len(w) > 4, words))
print("filter long  :", long_words)