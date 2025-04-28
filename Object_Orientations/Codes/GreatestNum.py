def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)  # Step 1: find the maximum candies
    result = []  # to store the answer

    for candy in candies:
        if candy + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)

    return result
