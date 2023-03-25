// 2023/03/25
// 내 코드의 문제점
// m의 크기가 커진다면 시간 초과 판정을 받음
n, m, k = map(int, input().split(' '))
arr = list(map(int, input().split()))

arr.sort()

result  = 0

for i in range(m):
  if (i+1)%k != 0:
    result += arr[n-1]
  else:
    result += arr[n-2]
    
print(result)


// 시간복잡도 고려해서 문제풀기!
n, m, k = map(int, input().split(' '))
arr = list(map(int, input().split()))

arr.sort()

first = arr[n-1]
second = arr[n-2]

count = int((m / (k+1)) * k + m % (k+1))

result = first * count + second * (m - count)
print(result)
