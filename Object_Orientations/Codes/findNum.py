def findNum(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1
    return count

print(findNum([12,898398,6,34]))
print(findNum([555, 901, 482, 1771])) 