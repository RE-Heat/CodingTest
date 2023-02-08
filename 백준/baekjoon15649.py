#백준 15649번 N과 M(1)

import itertools

N, M = input().split()
N = int(N)
M = int(M)

arr = []

for i in range(1, N + 1):
  arr.append(i)

if (M == 1):
  for x in arr:
    print(x)
else:
  nPr = itertools.permutations(arr, M)
  for x in nPr:
    print(*x)