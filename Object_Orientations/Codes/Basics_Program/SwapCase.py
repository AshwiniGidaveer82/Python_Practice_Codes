text = input()
swapped_text = " "
for char in text:
    if char.islower():
        swapped_text += char.upper()
    elif char.isupper():
        swapped_text += char.lower()
    else:
        swapped_text += char
print(swapped_text)


# Method 2 
text = "Hello World"
swapped_text = text.swapcase()
print(swapped_text)