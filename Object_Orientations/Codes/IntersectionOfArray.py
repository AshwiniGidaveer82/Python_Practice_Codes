# Intersection of Two Array(This will return the single element with removed duplicate elements)

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))  


print(intersection([1,2,2,1], [2,2]))       # Output: [2]
print(intersection([4,9,5], [9,4,9,8,4]))   # Output: [4,9] or [9,4]



# Intersection of Two Array(This will return the occurrence of matched elementsss)

from collections import Counter

def intersect(nums1, nums2):
    return list((Counter(nums1) & Counter(nums2)).elements())


print(intersect([1,2,2,1], [2,2]))       # Output: [2,2]
print(intersect([4,9,5], [9,4,9,8,4]))   # Output: [4,9] or [9,4]

