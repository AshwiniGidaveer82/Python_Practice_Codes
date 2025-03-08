def check_and_reverse(arr):
    n = len(arr)
    first_half_sum = sum(arr[:n//2])
    second_half_sum = sum(arr[n//2:])

    if first_half_sum < second_half_sum:
        arr.reverse()

    print(arr)

arr = [1,2,3,10,30,20]
print(check_and_reverse(arr))