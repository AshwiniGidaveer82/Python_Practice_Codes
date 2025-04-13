def sub_seq(s1, s2):
    return sorted(s1) == sorted(s2)
#     i = 0
#     for char in s2:
#         if i < len(s1) and s1(i) == char:
#             i += 1
#     return i == len(s1)

print(sub_seq("listen", "istlie12")) 


def is_anagram(s1, s2):
    return len(s1) == len(s2)

print(is_anagram("mom", "omo"))