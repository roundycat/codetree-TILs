def get_neighbors(x, y, n, grid):
    # 여덟방향의 인접한 위치 좌표
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = []
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            neighbors.append((nx, ny))
    
    return neighbors

def perform_turn(grid, n):
    # 위치별로 숫자의 위치를 찾기 위한 딕셔너리
    position = {}
    for i in range(n):
        for j in range(n):
            position[grid[i][j]] = (i, j)
    
    # 숫자 1부터 n*n까지 순서대로 처리
    for num in range(1, n * n + 1):
        x, y = position[num]  # 현재 숫자의 위치
        neighbors = get_neighbors(x, y, n, grid)  # 여덟방향 이웃 찾기
        
        # 인접한 숫자들 중 가장 큰 값 찾기
        max_pos = x, y
        max_value = grid[x][y]
        
        for nx, ny in neighbors:
            if grid[nx][ny] > max_value:
                max_value = grid[nx][ny]
                max_pos = nx, ny
        
        # 가장 큰 이웃과 값 교환
        if max_pos != (x, y):
            grid[x][y], grid[max_pos[0]][max_pos[1]] = grid[max_pos[0]][max_pos[1]], grid[x][y]
            # 위치 업데이트
            position[grid[x][y]] = (x, y)
            position[grid[max_pos[0]][max_pos[1]]] = max_pos

def solve(n, m, grid):
    # m번의 턴 수행
    for _ in range(m):
        perform_turn(grid, n)
    
    # 결과 출력
    for row in grid:
        print(" ".join(map(str, row)))

# 입력 처리
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 문제 해결
solve(n, m, grid)