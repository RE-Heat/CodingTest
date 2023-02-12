#백준 10819번 차이를 최대로

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

arr2 = []

perm = list(permutations(arr,N))

sum = 0
sumArr = []

for j in range(0, len(perm)):
  for i in range(0, N-1):
    sum = sum + abs(perm[j][i] - perm[j][i+1])
  sumArr.append(sum)
  sum = 0
  
print(max(sumArr))