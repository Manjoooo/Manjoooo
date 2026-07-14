n = int(input())

# 바깥 루프: 1번째 줄부터 n번째 줄까지
for i in range(1, n + 1):
    # 안쪽 루프: 각 줄마다 1번째 칸부터 i번째 칸까지
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()  # 한 줄 출력이 끝나면 줄바꿈