n = map(int, input())
arr = input().split()

x = 1
y = 1

for i in range(len(arr)):
  if arr[i] == 'L':
    if y == 1 :
      pass
    else:
      y -= 1
  if arr[i] == 'R':
    if y == 5 :
      pass
    else:
      y += 1
  if arr[i] == 'U':
    if x == 1 :
      pass
    else:
      x -= 1
  if arr[i] == 'D':
    if x == 5 :
      pass
    else:
      x += 1

print(x, y)

