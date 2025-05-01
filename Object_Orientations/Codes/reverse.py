def reverse(s):
    words = s.split(" ")
    reversed_string = words[::-1]
    return " ".join(reversed_string)

s = str(input())
print(reverse(s))
print(reverse("the sky is blue")) 