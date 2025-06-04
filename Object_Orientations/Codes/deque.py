from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        getattr(d, cmd[0])(cmd[1])
    else:
        getattr(d, cmd[0])()

print(*d)
