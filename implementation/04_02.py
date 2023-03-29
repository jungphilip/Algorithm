input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') +1

directions = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

cnt = 0

for direction in directions:
  if 0 <row + direction[0] < 9 and 0< column + direction[1] <9:
    cnt += 1

print(cnt)
