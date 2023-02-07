#백준2309 일곱난쟁이

dwarfs = []

#입력받은 값 리스트에 넣기
for _ in range(9):
  dwarfs.append(int(input()))

#list 총합
sumDwarfs = sum(dwarfs)

for i in range(0, 8):
  for j in range(1, 9):
    a = sumDwarfs - dwarfs[i] - dwarfs[j]
    if (a == 100):
      notDwarf1 = dwarfs[i]
      notDwarf2 = dwarfs[j]
      break

dwarfs.remove(notDwarf1)
dwarfs.remove(notDwarf2)

a = sorted(dwarfs)
for i in a:
  print(i)
