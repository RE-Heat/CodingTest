#백준 2851번 슈퍼마리오

arr = []

for _ in range(0, 10):
  arr.append(int(input()))

sum = 0
i = 0

#총합이 100이 넘는 i값 구하기
for i in range(0, 10):
  sum = sum + arr[i]
  if (sum >= 100):
    break

#arr[0] ~arr[i]까지 합
sumi = 0
for k in range(0, i + 1):
  sumi = sumi + arr[k]

#arr[0]~arr[i-1]까지 합
sumi2 = 0
for j in range(0, i):
  sumi2 = sumi2 + arr[j]

#조건식
if (abs(sumi - 100) == abs(sumi2 - 100)):
  print(max(sumi, sumi2))
elif (abs(sumi - 100) < abs(sumi2 - 100)):
  print(sumi)
else:
  print(sumi2)
