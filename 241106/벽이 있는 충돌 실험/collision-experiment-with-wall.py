# 방향 설정: U, D, R, L에 따라 이동 방향 정의
directions = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

def reverse_direction(d):
    # 벽에 부딪혔을 때 방향 반전
    if d == 'U': return 'D'
    elif d == 'D': return 'U'
    elif d == 'R': return 'L'
    elif d == 'L': return 'R'

def simulate_marbles(N, marbles):
    # 현재 구슬의 위치 및 방향 초기화
    active_marbles = {(x, y): d for x, y, d in marbles}
    previous_states = set()  # 이전 상태를 저장하여 반복 확인
    time = 0  # 경과 시간 초기화
    
    while True:
        # 현재 상태를 튜플 형태로 저장하여 반복되는지 확인
        state = tuple(sorted(active_marbles.items()))
        if state in previous_states:
            # 이전에 나온 상태라면 반복이므로 시뮬레이션 종료
            break
        previous_states.add(state)
        
        new_positions = {}  # 다음 위치를 저장

        # 구슬 이동
        for (x, y), d in active_marbles.items():
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            # 벽에 닿으면 방향 반전
            if nx < 1 or nx > N or ny < 1 or ny > N:
                d = reverse_direction(d)
                nx, ny = x, y  # 위치를 그대로 유지

            # 새로운 위치에 구슬 추가
            if (nx, ny) in new_positions:
                new_positions[(nx, ny)].append(d)  # 충돌 가능성 있는 위치
            else:
                new_positions[(nx, ny)] = [d]

        # 충돌 후 남은 구슬만 유지
        active_marbles = {}
        for pos, dirs in new_positions.items():
            if len(dirs) == 1:  # 충돌이 없다면 구슬 유지
                active_marbles[pos] = dirs[0]

        # 더 이상 이동할 구슬이 없으면 종료
        if not active_marbles:
            break
        
        time += 1  # 경과 시간 증가

    # 남아있는 구슬의 개수 반환
    return len(active_marbles)

# 입력 처리 및 실행
T = int(input().strip())
results = []
for _ in range(T):
    N, M = map(int, input().strip().split())
    marbles = [tuple(input().strip().split()) for _ in range(M)]
    marbles = [(int(x), int(y), d) for x, y, d in marbles]
    results.append(simulate_marbles(N, marbles))

# 결과 출력
for result in results:
    print(result)