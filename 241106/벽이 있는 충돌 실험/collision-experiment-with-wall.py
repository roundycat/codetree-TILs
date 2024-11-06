# 방향 설정: U, D, R, L에 따라 이동 방향 정의
directions = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

def simulate_marbles(N, marbles):
    active_marbles = {(x, y): d for x, y, d in marbles}  # 현재 위치와 방향을 저장
    max_time = N * N  # 충분히 긴 시간 동안만 시뮬레이션
    
    for _ in range(max_time):
        new_positions = {}  # 다음 위치 저장

        # 구슬 이동
        for (x, y), d in active_marbles.items():
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            # 벽에 닿으면 방향 반전
            if nx < 1 or nx > N or ny < 1 or ny > N:
                if d == 'U': d = 'D'
                elif d == 'D': d = 'U'
                elif d == 'R': d = 'L'
                elif d == 'L': d = 'R'
                nx, ny = x, y  # 제자리에 그대로 유지

            # 새로운 위치에 구슬 추가
            if (nx, ny) in new_positions:
                new_positions[(nx, ny)].append(d)  # 같은 위치에 구슬 추가 (충돌 발생 가능)
            else:
                new_positions[(nx, ny)] = [d]
        
        # 충돌 구슬 제거 후 남은 구슬만 유지
        active_marbles = {}
        for pos, dirs in new_positions.items():
            if len(dirs) == 1:
                active_marbles[pos] = dirs[0]  # 충돌이 없으면 그대로 유지

        # 남은 구슬이 없으면 종료
        if not active_marbles:
            break

    # 남아있는 구슬의 수 반환
    return len(active_marbles)

# 입력 처리 및 실행
T = int(input().strip())
results = []
for _ in range(T):
    N, M = map(int, input().strip().split())
    marbles = [tuple(input().strip().split()) for _ in range(M)]
    # x, y를 정수로, d는 그대로 저장
    marbles = [(int(x), int(y), d) for x, y, d in marbles]
    results.append(simulate_marbles(N, marbles))

# 결과 출력
for result in results:
    print(result)