def subsets(nums):
    result = [[]]  

    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num]) 
        result.extend(new_subsets)  
    return result

print(subsets([1,2,3]))  # Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
print(subsets([0]))      # Output: [[], [0]]
