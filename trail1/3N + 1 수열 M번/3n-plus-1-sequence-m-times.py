
m = int(input())

for _ in range(m):
    n = int(input())
    
    count = 0 
    
    while n != 1:
        if n % 2 == 0:
            # 짝수일 때
            n = n // 2
        else:
            # 홀수일 때
            n = n * 3 + 1
        
        # 연산을 한 번 수행했으므로 횟수를 1 증가시킵니다.
        count += 1
        
    # 최종적으로 계산된 연산 횟수를 출력합니다.
    print(count)