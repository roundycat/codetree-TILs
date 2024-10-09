# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
answer = [
    [0] * m
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0           # 시작은 (0, 0) 입니다.
dir_num = 1           # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

# 처음 시작 위치에 초기값을 적습니다.
answer[x][y] = 1

# n*m번 진행합니다.
for i in range(2, n * m + 1):
    # 나아갈 수 있을때까지 방향을 바꿔가며 확인해봅니다. 
    while True:           
        # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
        # 그 위치로 나아갈 수 있는지 확인합니다.
        if in_range(nx, ny) and answer[nx][ny] == 0:
            # 나아갈 수 있다면 위치를 갱신해주고 배열에 올바른 값을 채워넣습니다.
            x, y = nx, ny
            answer[x][y] = i
            break
        else:
            # 나아갈 수 없다면 반시계방향으로 90'를 회전하여 
            # 그 다음 방향을 확인해봐야 합니다.
            dir_num = (dir_num + 3) % 4

# 출력:
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()