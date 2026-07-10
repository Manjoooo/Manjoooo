# 변수 선언 및 입력
n = int(input())
cnt = 9
    
# cnt를 이용해 n칸의 정사각형에 올바른 숫자를 출력합니다.
for _ in range(n):
    for _ in range(n):
        print(cnt, end="")
        cnt -= 1
        if cnt == 0:
            cnt = 9
    print()