# 전체 테스트케이스 개수 N을 입력받습니다.
n = int(input())

for _ in range(n):
    # 각 케이스의 a와 b를 입력받습니다.
    a, b = map(int, input().split())
    
    even_sum = 0  # 짝수들의 합을 저장할 변수 (매 케이스마다 0으로 초기화)
    
    # a부터 b까지(b를 포함하므로 b + 1까지) 검사합니다.
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_sum += i
            
    # 결과를 출력합니다.
    print(even_sum)