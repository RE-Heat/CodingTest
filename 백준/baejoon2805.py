#백준 2805번 나무자르기
import sys

input = sys.stdin.readline


#이진탐색
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    sum_list = [max(0, x - mid) for x in tree]
    total_sum = sum(sum_list)

    if total_sum == target:
      return mid
    elif total_sum < target:
      end = mid - 1
    else:
      start = mid + 1
  return end


N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

result1 = binary_search(tree, M, 0, tree[-1])
print(result1)
