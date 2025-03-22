from collections import Counter

def unique_occurrences(arr):
    freq = Counter(arr)
    return len(set(freq.values())) == len(freq)


print(unique_occurrences([1, 2, 2, 1, 1, 3]))  # Output: True
print(unique_occurrences([1, 2]))              # Output: False
print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # Output: True
