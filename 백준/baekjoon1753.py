#백준 1753 최단경로
import sys
from queue import PriorityQueue
input = sys.stdin.readline

#정점개수 간선 개수
V, E = map(int, input().split())
K = int(input()) #시작점

distance = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
  u, v, w = map(int, input().split())
  myList[u].append((v, w))

#0으로 자동정렬하기 위해 q값에 가중치 w를 먼저 삽입. K는 시작점
q.put((0, K))
distance[K] = 0

while q.qsize()>0:
  current = q.get()
  c_v = current[1]
  if visited[c_v]:
    continue
  visited[c_v] = True
  for temp in myList[c_v]:
    next = temp[0] #인접리스트는 v먼저 넣었으므로 인덱스 0
    value = temp[1] #가중치
    if distance[next] > distance[c_v] + value:
      distance[next] = distance[c_v] + value
      q.put((distance[next], next))

for i in range(1, V+1):
  if visited[i]:
    print(distance[i])
  else:
    print("INF")