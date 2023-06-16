#백준 1062번 가르침
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

if k < 5:
  print(0)
  exit()
elif k == 26:
  print(n)
  exit()

ans = 0
words = [set(input().rstrip()) for _ in range(n)]
learn = [0] * 26

for ch in ("a", "c", "i", "n", "t"):
  learn[ord(ch)-ord("a")] = 1

def dfs(idx, cnt):
  global ans
  if cnt == k-5:
    readcnt = 0
    for word in words:
      check = True
      for w in word:
        if not learn[ord(w) - ord("a")]:
          check = False
          break
      if check:
        readcnt +=1
    ans = max(ans, readcnt)
    return
  for i in range(idx, 26):
    if not learn[i]:
      learn[i] = True
      dfs(i, cnt+1)
      learn[i] = False

dfs(0, 0)
print(ans)