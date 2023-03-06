#백준 16198번 에너지 모으기
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = 0

def dfs(tmp):
  global answer

  if len(arr)==2:
    answer = max(answer, tmp)
    return
  else:
    for i in range(1, len(arr)-1):
      k = arr[i]
      del arr[i]
      dfs(tmp + arr[i-1] * arr[i])
      arr.insert(i, k)
    
dfs(0)
print(answer)