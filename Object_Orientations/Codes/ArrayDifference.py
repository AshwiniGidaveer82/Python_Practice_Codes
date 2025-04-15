def array_diff(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    nums1 = list(set1 - set2)
    nums2 = list(set2 - set1)

    return [nums1, nums2]

nums1 = [1,2,3,4,4]
nums2 = [2,3,4,5,6,7]
print(array_diff(nums1, nums2))


# Second Method 

def arr_diff(nums1,  nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return [list(set2 - set1) , list(set1 - set2)]

nums1 = [1,2,3,4,5]
nums2 = [2,3,4,5,6,7,8]
print(arr_diff(nums1, nums2))