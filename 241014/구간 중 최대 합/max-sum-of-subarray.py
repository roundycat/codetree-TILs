# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 모든 구간의 시작점을 잡아봅니다.
max_sum = 0
for i in range(0, n - k + 1):
    # 해당 구간 내 원소의 합을 구합니다.
    interval_sum = 0
    for j in range(i, i + k):
        interval_sum += arr[j]

    # 최댓값을 구합니다.
    max_sum = max(max_sum, interval_sum)
                        
print(max_sum)