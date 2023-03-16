#백준 10845번 큐
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
ans = deque([])

for _ in range(N):
  cmd = list(map(str, input().split()))
  if cmd[0]== 'push':
    ans.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if ans:print(ans.popleft())
    else: print(-1)
  elif cmd[0] == 'front':
    if ans:print(ans[0])
    else: print(-1)
  elif cmd[0] == 'back':
    if ans:print(ans[-1])
    else: print(-1)
  elif cmd[0] == 'size':
    print(len(ans))
  elif cmd[0] == 'empty':
    if ans:print(0)
    else: print(1)