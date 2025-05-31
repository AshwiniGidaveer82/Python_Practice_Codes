import os
from collections import Counter

def sortBugReportFrequencies(bugs):
    freq = Counter(bugs)
    sorted_bugs = sorted(bugs, key=lambda bug: (freq[bug], bug))

    return sorted_bugs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bugs_count = int(input().strip())
    bugs = []

    for _ in range(bugs_count):
        bugs_item = int(input().strip())
        bugs.append(bugs_item)

    result = sortBugReportFrequencies(bugs)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
