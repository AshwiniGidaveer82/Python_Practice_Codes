def compress(chars):
    write = 0  
    i = 0      

    while i < len(chars):
        char = chars[i]
        count = 0

      
        while i < len(chars) and chars[i] == char:
            i += 1
            count += 1

       
        chars[write] = char
        write += 1

        
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write
chars = ["a","a","b","b","c","c","c"]
length = compress(chars)
print(length)        # Output: 6
print(chars[:length])  # Output: ['a', '2', 'b', '2', 'c', '3']
