#백준 15686번 치킨 배달
import sys
from itertools import combinations

input = sys.stdin.readline

#문제 담기
N, M = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(N))

#집, 치킨집 좌표 담기
result = float("inf")
home = []
chicken = []

for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      home.append([i+1, j+1])
    elif city[i][j] == 2:
      chicken.append([i+1, j+1])

      
#치킨거리 찾기
for chick in combinations(chicken, M):
  temp = 0
  for a in home:
    chick_len = float("inf")
    for b in range(M):
      chick_len = min(chick_len, abs(a[0] - chick[b][0]) + abs(a[1] - chick[b][1]))                
    temp += chick_len
  result = min(result, temp)  

print(result)