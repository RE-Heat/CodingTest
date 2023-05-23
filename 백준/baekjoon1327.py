#백준 1327번: 소트 게임
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
arr = list(input().split())

visited = set("".join(arr))
target = sorted(arr)

q = deque([])
q.append((arr, 0))

ans = -1

while q:
  arr, cnt = q.popleft()

  if arr == target:
    ans = cnt
    break
  
  for i in range(n-k+1):
    rarr = arr[i:i+k]
    rarr.reverse()
    narr = arr[:i] + rarr + arr[i+k:]
    str = "".join(narr)
    if str not in visited:
      visited.add(str)
      q.append((narr, cnt+1))

print(ans)