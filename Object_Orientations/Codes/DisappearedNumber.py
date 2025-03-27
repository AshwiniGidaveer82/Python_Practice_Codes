def find_disappeared_numbers(nums):
    n = len(nums)
    complete_set = set(range(1, n + 1))
    nums_set = set(nums)
    missing_numbers = list(complete_set - nums_set)
    return missing_numbers


nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_disappeared_numbers(nums1))  # Output: [5, 6]

nums2 = [1, 1]
print(find_disappeared_numbers(nums2))  # Output: [2]
