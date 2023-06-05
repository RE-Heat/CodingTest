#백준 1931번 회의실
import sys
input = sys.stdin.readline

N = int(input())
session = []
for _ in range(N):
  session.append(list(map(int, input().split())))

session.sort(key = lambda x:(x[1], x[0]))

cnt = 1
a = 0

for j in range(1, N):  
  if session[a][1] <= session[j][0]:
    cnt +=1
    a = j   

print(cnt)