from collections import defaultdict

def maxOperations(nums, k):
    count = defaultdict(int)
    operations = 0

    for num in nums:
        complement = k - num
        if count[complement] > 0:
            operations += 1
            count[complement] -= 1
        else:
            count[num] += 1

    return operations
print(maxOperations([1, 2, 3, 4], 5))        # Output: 2
print(maxOperations([3, 1, 3, 4, 3], 6))     # Output: 1
