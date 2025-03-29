def height_checker(heights):
    expected = sorted(heights)
    
    mismatch_count = 0
    
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            mismatch_count += 1
    
    return mismatch_count

print(height_checker([1, 1, 4, 2, 1, 3]))  # Output: 3
print(height_checker([5, 1, 2, 3, 4]))    # Output: 5
print(height_checker([1, 2, 3, 4, 5]))    # Output: 0
