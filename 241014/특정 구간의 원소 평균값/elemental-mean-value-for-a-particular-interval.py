# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

# 모든 구간을 잡아봅니다.
cnt = 0
for i in range(n): # 구간의 시작점을 잡아봅니다.
    for j in range(i, n): # 구간의 끝점을 잡아봅니다.
        # 구간 [i, j] 내 원소의 합을 구합니다.
        sum_interval = 0
        for k in range(i, j + 1):
            sum_interval += arr[k]

        # 평균을 구합니다.
        avg = sum_interval / (j - i + 1)

        # 구간 내에 원소 평균값과 동일한 원소가 있으면 개수를 세줍니다.
        exists = False
        for k in range(i, j + 1):
            if arr[k] == avg:
                exists = True

        if exists:
            cnt += 1
                        
print(cnt)