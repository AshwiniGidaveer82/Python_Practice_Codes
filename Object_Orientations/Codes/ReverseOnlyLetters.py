def reverseOnlyLetters(s):
    letters = [c for c in s if c.isalpha()]  
    return "".join(c if not c.isalpha() else letters.pop() for c in s)  


print(reverseOnlyLetters("ab-cd"))         # Output: "dc-ba"
print(reverseOnlyLetters("a-bC-dEf-ghIj")) # Output: "j-Ih-gfE-dCba"
print(reverseOnlyLetters("Test1ng-Leet=code-Q!")) # Output: "Qedo1ct-eeLg=ntse-T!"
