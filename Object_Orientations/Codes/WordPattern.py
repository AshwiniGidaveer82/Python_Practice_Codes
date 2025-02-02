from itertools import zip_longest

def wordPattern(self, pattern: str, s: str) -> bool:
    s = s.split()
    return (len(set(pattern)) ==
            len(set(s)) ==
            len(set(zip_longest(pattern,s))))

print(wordPattern("abba", "dog cat cat dog")) 
