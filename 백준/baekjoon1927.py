#백준 1927 최소 힙
import sys
import heapq
input = sys.stdin.readline

n = int(input())
min_heap = []

for _ in range(n):
  num = int(input())
  if num == 0:
    if len(min_heap):
      print(heapq.heappop(min_heap))
    else:
      print(0)
  else:
    heapq.heappush(min_heap, num)

#최대힙
# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# max_heap = []

# for _ in range(n):
#   num = int(input())
#   if num == 0:
#     if len(max_heap):
#       print(-heapq.heappop(max_heap))
#     else:
#       print(0)
#   else:
#     heapq.heappush(max_heap, -num)
