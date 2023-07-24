#백준 1038번 감소하는 수
import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = [i for i in range(10)]
ans = []

for i in range(1, 11):
  for j in combinations(arr, i):
    temp = ''.join(list(map(str, reversed(list(j)))))
    ans.append(int(temp))

ans.sort()

if n >= len(ans):
  print(-1)
else:
  print(ans[n])