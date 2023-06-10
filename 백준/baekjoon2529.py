#백준 2529번 부등호
import sys
input = sys.stdin.readline

#DFS로 푸는 방식
def check(a, b, op):
  if op == '<':
    return a < b
  else:
    return a > b

def dfs(cnt, num):
  print(cnt, num)
  if cnt == n+1:
    ans.append(num)
    return
  for i in range(10):
    if visited[i]: continue
    if cnt == 0 or check(num[cnt-1], str(i), sign[cnt-1]):      
      visited[i] = 1
      dfs(cnt+1, num+str(i))
      visited[i] = 0      

n = int(input())
sign = list(input().split())
visited = [0] * 10
ans = []
dfs(0, '')
ans.sort()
print(ans)
print(ans[-1])
print(ans[0])