#백준 2170 선 긋기
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])

start, end = arr[0][0], arr[0][1]
ans = 0

for i in range(1, N):
  now_start, now_end = arr[i]   
  #겹칠 때
  if end >= now_start:
    end = max(end, now_end)
  
  #안 겹칠 때
  if end < now_start:
    ans += end - start
    start, end = now_start, now_end

ans += end - start
print(ans)