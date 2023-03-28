#백준 1676번 팩토리얼 0의 개수
import sys
input = sys.stdin.readline

N = int(input())
num = 1

#팩토리얼 구하기
for i in range(N):
  num = num * (i + 1)

#팩토리얼 구하고 문자열로 변환 후 뒤집기
findZero = reversed(str(num))

#첫 문자열부터 0인지 확인 후 count 세기
cnt = 0

for a in findZero:
  if a == '0':
    cnt += 1
  else:
    break

print(cnt)

#5, 15, 125
