#백준 2961번 도영이가 만든 맛있는 음식
#감이 안와서 답봄.

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
sour = []
bitter = []

#신맛, 쓴맛 배열에 담기
for _ in range(N):
  a, b = map(int, input().split())
  sour.append(a)
  bitter.append(b)

diff = float("inf")
  
#나올 수 있는 경우의 수 담기
for i in range(1, N+1):
  index = list(combinations(list(range(N)),i))
  print(index)
  
  for food in index:
    s=1
    b=0
    
    for j in range(i):
      s = s * sour[food[j]]
      b = b + bitter[food[j]]
    if abs(s-b) < diff:
      diff = abs(s-b)


print(diff)