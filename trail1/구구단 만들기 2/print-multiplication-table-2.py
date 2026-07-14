inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])

# 바깥쪽 루프: 곱해지는 수 (1부터 9까지 가로줄 형성)
for i in range(2, 9, 2):
    # 안쪽 루프: 단수 (b단부터 a단까지 -2씩 감소)
    for j in range(b, a - 1, -1):
        print(f"{j} * {i} = {j * i}", end="")
        
        # 현재 출력한 단(j)이 마지막 단(a)이 아닐 때만 우측에 슬래시 구분자 추가
        if j > a:
            print(" / ", end="")
            
    print()  