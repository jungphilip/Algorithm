# 내 코드 (지저분)
n = int(input())
con_sec = (n+1)*3600 - 1
cnt = 0

for i in range(con_sec):
  # OO시 OO분 O3초인 경우
  if i % 10 == 3:
    cnt += 1
  # OO시 OO분 3O초인 경우
  elif i % 3600 % 60 // 10 == 3:
    cnt += 1
  # OO시 O3분 OO초인 경우
  elif i % 3600 // 60 % 10 == 3:
    cnt += 1
  # OO시 3O분 OO초인 경우
  elif i % 3600 // 60 // 10 == 3:
    cnt += 1
  # O3시 OO분 OO초인 경우
  elif i // 3600 % 10 == 3:
    cnt +=1

print(cnt)



# 책 코드 (훨씬 간결함)
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
