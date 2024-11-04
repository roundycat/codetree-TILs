def find_max_positive_rectangle(matrix, n, m):
    max_area = -1

    # Iterate over all possible top-left corners of the sub-rectangles
    for start_row in range(n):
        for start_col in range(m):
            # Iterate over all possible bottom-right corners of the sub-rectangles
            for end_row in range(start_row, n):
                for end_col in range(start_col, m):
                    # Check if all values in the current rectangle are positive
                    is_positive = True
                    for i in range(start_row, end_row + 1):
                        for j in range(start_col, end_col + 1):
                            if matrix[i][j] <= 0:
                                is_positive = False
                                break
                        if not is_positive:
                            break
                    
                    # Calculate area if the rectangle is valid
                    if is_positive:
                        area = (end_row - start_row + 1) * (end_col - start_col + 1)
                        max_area = max(max_area, area)

    return max_area

# Read input
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find and print the result
result = find_max_positive_rectangle(matrix, n, m)
print(result)