from functools import reduce
 
nums = [4, 7, 1, 9, 3, 6, 2, 8, 5]
words = ["banana", "apple", "cherry", "date"]
squares = list(map(lambda x: x ** 2, nums))
print("\nmap squares  :", squares)
 
upper = list(map(str.upper, words))
print("map upper    :", upper)