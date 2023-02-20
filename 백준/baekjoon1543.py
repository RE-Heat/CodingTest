#백준 1543번 문서검색
#input()옆에 띄어쓰기 안오도록 rstrip()필수
#파이썬 슬라이싱 활용 (index 범위 헷갈림)

import sys

input = sys.stdin.readline

doc = input().rstrip()
search = input().rstrip()

cnt = 0
index = 0

for i in range(len(doc)):
  if index > i:
    continue

  if search == doc[i:i+len(search)]:
    cnt +=1
    index = i+len(search)

print(cnt)