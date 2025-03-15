def char_check(ch):
    vowels = "aeiouAEIOU"
    if ch.isalpha():
        if ch in vowels:
            print(f"{ch} is a vowel")
        else:
            print(f"{ch} is consonant")
    else:
        print("Invalid characters")
ch = input("Enter a character: ")
print(char_check(ch))