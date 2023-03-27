n = map(int, input())
arr = input().split()

x = 1
y = 1

for i in range(len(arr)):
  if arr[i] == 'L':
    if y != 1 :
      y -= 1
  if arr[i] == 'R':
    if y != n :
      y += 1
  if arr[i] == 'U':
    if x != 1 :
      x -= 1
  if arr[i] == 'D':
    if x != n :
      x += 1

print(x, y)

