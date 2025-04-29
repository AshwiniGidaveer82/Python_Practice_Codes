def largestAltitude(gain):
    altitude = 0
    highest = 0

    for g in gain:
        altitude += g
        highest = max(highest, altitude)

    return highest

print(largestAltitude([-5,1,5,0,-7]))   # Output: 1
print(largestAltitude([-4,-3,-2,-1,4,3,2]))  # Output: 0
