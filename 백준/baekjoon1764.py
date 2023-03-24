#백준 1764번 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

unHear = []
unSeen = []

for _ in range(N):
  unHear.append(input().rstrip())

for _ in range(M):
  unSeen.append(input().rstrip())

unKnown = list(set(unHear) & set(unSeen))
unKnown.sort()

print(len(unKnown))
for i in unKnown:
  print(i)
