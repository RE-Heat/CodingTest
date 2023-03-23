#백준 10816번 숫자 카드 2

from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
num = list(map(int, input().split()))

cnt = Counter(cards)

output = []
for i in num:
  output.append(str(cnt[i]) if i in cnt else '0')

print(' '.join(output))

#방법1 collections Counter 사용(시간초과)
# import sys

# input = sys.stdin.readline
# from collections import Counter

# N = int(input())
# cards = tuple(map(int, input().split()))

# M = int(input())
# num = tuple(map(int, input().split()))

# cnt = Counter(cards)

# for i in range(M - 1):
#   print(" ".join(f'{cnt[num[i]]}') if num[i] in cards else '0', end=" ")

# print(" ".join(f'{cnt[num[M-1]]}') if num[M - 1] in cards else '0')

#방법2 이진탐색 활용 [시간초과]
# import sys

# input = sys.stdin.readline

# N = int(input())
# cards = list(map(int, input().split()))

# M = int(input())
# num = list(map(int, input().split()))

# cards.sort()

# def binary_search(target, data):
#   start = 0
#   end = len(data) - 1
#   while start <= end:
#     mid = (start + end) // 2

#     if data[mid] == target:
#       return cards.count(target)
#     elif data[mid] < target:
#       start = mid + 1
#     elif data[mid] > target:
#       end = mid - 1
#   return 0

# for i in range(M - 1):
#   print(binary_search(num[i], cards), end=" ")

# #마지막
# print(binary_search(num[M - 1], cards), end="")
