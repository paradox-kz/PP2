from functools import reduce
 
nums = [4, 7, 1, 9, 3, 6, 2, 8, 5]
words = ["banana", "apple", "cherry", "date"]
product = reduce(lambda a, b: a * b, nums)
print("\nreduce product:", product)    # 4*7*1*...*5
 
max_val = reduce(lambda a, b: a if a > b else b, nums)
print("reduce max    :", max_val)      # 9