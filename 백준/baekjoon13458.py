#백준 13458번 시험감독
#총감독이 시험장 응시자수보다 많은 사람 감독할 경우도 고려해야 함.

import sys
import math
input = sys.stdin.readline

N = int(input())
arr = []

arr = list(map(int, input().split()))

B, C = map(int, input().split())

sum = 0

for i in range(N):
  if(B<=arr[i]):
    sum = sum + math.ceil((arr[i]-B)/C)

print(N+sum)
