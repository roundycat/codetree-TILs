MAX_NUM = 10000

# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)
    
    arr[x] = 1 if c == 'G' else 2


# 모든 구간의 시작점을 잡아봅니다.
max_sum = 0
for i in range(MAX_NUM - k + 1):
    # 해당 구간 내 원소의 합을 구합니다.
    sum_interval = 0
    for j in range(i, i + k + 1):
        sum_interval += arr[j]

    # 최댓값을 구합니다.
    max_sum = max(max_sum, sum_interval)
                        
print(max_sum)