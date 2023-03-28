#백준 17219번 비밀번호 찾기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sitePW = {}

#사이트 주소와 비번 넣기
for _ in range(N):
  site, pw = input().split()
  sitePW[site] = pw

#비번 찾을 주소 넣기
for _ in range(M):
  find = input().rstrip()
  print(sitePW[find])
