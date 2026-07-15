n = int(input())

for i in range(1, n + 1):
    row_items = []
    # i번째 행에서는 1부터 (n - i + 1)까지 곱합니다.
    for j in range(1, n - i + 2):
        row_items.append(f"{i} * {j} = {i * j}")
    
    # 각 항들을 " / "로 연결하여 출력합니다.
    print(" / ".join(row_items))