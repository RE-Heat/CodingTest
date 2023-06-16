#백준 15903번 카드 합체 놀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(M):
  #오름차순 정렬
  arr.sort()  
  #첫 번째 + 두 번째 값 합
  temp = arr[0] + arr[1]  
  #계산 값 두 장 모두에 덮어 쓰기
  arr[0] = temp
  arr[1] = temp

#n장 카드에 쓰여있는 수를 모두 더한 값
print(sum(arr))
