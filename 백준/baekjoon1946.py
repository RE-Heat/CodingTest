#백준 1946번 신입사원
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  newbie = [list(map(int, input().split())) for _ in range(N)]
  newbie.sort()
  flag = newbie[0][1]
  cnt = 1
  for i in range(1, N):
    if newbie[i][1] < flag:
      cnt +=1
      flag = newbie[i][1]
  print(cnt)