def isPerfectSquare(num):
    left, right = 1, num

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


print(isPerfectSquare(16))  # Output: True
print(isPerfectSquare(14))  # Output: False
