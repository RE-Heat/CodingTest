#백준 11050 이항 계수 1
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

#팩토리얼 구하기
numerator  = 1
for i in range(K):
  numerator  *= N
  N -= 1

#나눌 값
denominator = 1

for i in range(2, K+1):
  denominator *= K
  K -=1

print(numerator//denominator)