#백준 2164번 카드2
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [i + 1 for i in range(N)]
cards = deque(arr)

while len(cards) > 1:
  #첫 번째 카드 제거
  cards.popleft()

  #두 번째 카드 빼고 밑으로 넣기
  second = cards.popleft()
  cards.append(second)

print(*cards)