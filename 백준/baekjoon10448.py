#백준 10448번 유레카 이론

n = int(input())
arr = []

for m in range(0, n):
  arr.append(int(input()))

#삼각함수값 trinums에 담기
trinums = [0]

for i in range(1, 45):
  trinums.append(int((i*(i+1))/2))

def Eureka(nums):
  for j in range(1, 45):
     for k in range(1, 45):
       for l in range(1, 45):        
        if(nums==trinums[j]+trinums[k]+trinums[l]):
          return 1
  return 0      

for a in range(0, n):
  print(Eureka(arr[a]))