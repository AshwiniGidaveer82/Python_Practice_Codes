from collections import defaultdict

def group_word_positions():
    n, m = map(int, input().split())  
    d = defaultdict(list)

    for i in range(n):
        word = input()
        d[word].append(i + 1)

    for _ in range(m):
        word = input()
        if word in d:
            print(' '.join(map(str, d[word])))
        else:
            print(-1)
            
group_word_positions()
