def proSum(n):
    sum = 0
    product = 1
    while n != 0:
        digit = n % 10
        sum += digit
        product *= digit 
        n = n // 10
    return product - sum
    
print(proSum(123))



# def subtract_product_and_sum(n):
#     total_sum = 0
#     product = 1
    
#     while n != 0:
#         digit = n % 10
#         total_sum += digit
#         product *= digit
#         n = n // 10  
    
#     return product - total_sum

# print(subtract_product_and_sum(234))   # Output: 15
# print(subtract_product_and_sum(4421))  # Output: 21


 