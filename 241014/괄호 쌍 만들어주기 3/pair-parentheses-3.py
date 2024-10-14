# 변수 선언 및 입력
string = input()
n = len(string)

# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if string[i] == '(' and string[j] == ')':
            cnt += 1
            
print(cnt)