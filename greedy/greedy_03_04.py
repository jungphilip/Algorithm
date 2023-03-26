# 내 답안
n, k = map(int, input().split())
cnt = 0

while n != 1:
  cnt += 1
  if (n % k) != 0:
    n -= 1
  else:
    n = int(n/k)

print(cnt)

# 교재 답안
n, k = map(int, input().split())
result = 0

while True:
  # (N==K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
  target = (n//k) *k
  result += (n-target)
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break

  # K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

# 내 코드와의 차이점 : 시간복잡도
