count = 0
n = int(input())
while n > 0:
  for j in range(0, n):
    count += 1

  n//=2

print (count)
