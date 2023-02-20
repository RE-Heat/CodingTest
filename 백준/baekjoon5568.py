#백준 5568번 카드놓기
#set함수(중복제거)와 join함수(리스트를 문자열로 합쳐줌)

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
arr = []

for _ in range(N):
  arr.append(input().rstrip())

ans = set()

for per in permutations(arr, K):
  ans.add("".join(per))

print(len(ans))