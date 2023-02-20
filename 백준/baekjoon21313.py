import sys
input = sys.stdin.readline

#짝수 12121212
#홀수 1212123

N = int(input())
onetwo ="1 2 "

even = int(N/2)

if(N%2==0):
  print(onetwo*even)
else:
  print(onetwo*even+"3")