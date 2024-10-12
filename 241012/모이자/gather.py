def find_min_distance(arr):
    n = len(arr)
    
    # 집들의 좌표와 거주 인구를 기반으로 중앙값을 구함
    total_people = sum(arr)
    cumulative_people = 0
    median_house = 0
    
    # 누적된 사람 수를 기준으로 중앙값 찾기
    for i in range(n):
        cumulative_people += arr[i]
        if cumulative_people >= total_people // 2:
            median_house = i
            break

    # 중앙값 위치에 모두 모였을 때의 이동 거리 계산
    min_dist = 0
    for i in range(n):
        min_dist += abs(i - median_house) * arr[i]

    return min_dist

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 결과 출력
print(find_min_distance(arr))