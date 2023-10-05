#백준 20920번 영단어 암기는 괴로워
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
str_list = {}

#길이가 M이상인 단어만 외운다.
for _ in range(N):
  str = input().rstrip()
  if len(str) < M:
    continue
  else:
    if str in str_list:
      str_list[str] += 1
    else:
      str_list[str] = 1

#자주 나오는 단어일수록 앞에 배치
#해당 단어의 길이가 길수록 앞에 배치
#알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치
ans = sorted(str_list.items(), key = lambda x:(-x[1], -len(x[0]), x[0]))
for i, j in ans:
  print(i, end = "\n")
