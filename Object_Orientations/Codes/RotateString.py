def rotateString(s, goal):
    return len(s) == len(goal) and goal in (s + s)

print(rotateString("abcde", "cdeab"))  # Output: True
print(rotateString("abcde", "abced"))  # Output: False
