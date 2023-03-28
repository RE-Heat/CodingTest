#백준 1620번 포켓몬
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}

#포켓몬 이름과 번호
for i in range(1, N+1):
  Name = input().rstrip()
  pokemon[Name] = i

pokemon_list = list(pokemon)

#비번 찾을 주소 넣기
for _ in range(M):
  find = input().rstrip()
  if find.isalpha():
    print(pokemon[find])
  else:
    print(pokemon_list[int(find)-1])