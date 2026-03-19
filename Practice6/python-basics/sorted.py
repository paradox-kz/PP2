from functools import reduce
 
nums = [4, 7, 1, 9, 3, 6, 2, 8, 5]
words = ["banana", "apple", "cherry", "date"]
print("\nsorted(nums)             :", sorted(nums))
print("sorted(nums, reverse=True):", sorted(nums, reverse=True))
print("sorted(words, key=len)    :", sorted(words, key=len))