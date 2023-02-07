#백준 6679번 상기한 네자리 숫자

def convert(a, b):
  sum = 0
  while a > 0:
    sum = sum + a % b 
    a = a //b
  return sum  

for i in range(1000, 10000):
  d = convert(i, 10)
  e = convert(i, 12)
  f = convert(i, 16)
  if(d==e==f):
    print(i)