#백준 15651번 N과 M(3)

N, M = map(int, input().split())

rs = []

def recur(num):
  if num == M:
    print(*rs)
    return
  for i in range(1, N+1):
      rs.append(i)
      recur(num+1)
      rs.pop()
    
recur(0)
