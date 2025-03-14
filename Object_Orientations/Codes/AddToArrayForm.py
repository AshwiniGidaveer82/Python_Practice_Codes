def addToArrayForm(num, k):
    res = []
    i = len(num) - 1
    
    while i >= 0 or k > 0:
        if i >= 0:
            k += num[i] 
            i -= 1
        res.append(k % 10)  
        k //= 10  

    return res[::-1]  


print(addToArrayForm([1,2,0,0], 34))   # Output: [1,2,3,4]
print(addToArrayForm([2,7,4], 181))    # Output: [4,5,5]
print(addToArrayForm([2,1,5], 806))    # Output: [1,0,2,1]
