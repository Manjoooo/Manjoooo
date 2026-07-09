n = int(input())

for i in range(n): 
    # 1. 왼쪽 별 출력 (n - i개)
    for j in range(n - i):
        print("*", end="")
        
    # 2. 가운데 공백 출력 (2 * i개)
    for j in range(2 * i):
        print(" ", end="")
        
    # 3. 오른쪽 별 출력 (n - i개)
    for j in range(n - i):
        print("*", end="")
    
    print()

 # 양쪽에서 하니까 대칭으로...    