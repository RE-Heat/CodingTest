#백준 1439번 뒤집기

import sys
import math
input = sys.stdin.readline

S = input().rstrip()

#0숫자 다발, 1숫자 다발 찾기

cnt = 0

for i in range(len(S)-1):
  if(S[i]!=S[i+1]):
    cnt += 1

#모두 한 가지 숫자일 경우
if len(set(S))==1:
  print(0)
else:
  print(math.ceil(cnt/2))