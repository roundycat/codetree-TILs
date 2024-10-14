# 변수 선언 및 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 모든 쌍을 다 잡아봅니다.
max_cnt = 0
for i in range(n):
    # 격자를 벗어나지 않을 범위로만 잡습니다.
    for j in range(n - 2):
        cnt = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        max_cnt = max(max_cnt, cnt)
    
print(max_cnt)