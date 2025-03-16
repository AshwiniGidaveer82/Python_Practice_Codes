def sumZero(n):
    result = []
    
    for i in range(1, n // 2 + 1):
        result.append(i)   
        result.append(-i)  
    
    if n % 2 == 1:
        result.append(0)  
    
    return result

n = int(input("Enter n: "))
print(sumZero(n))
