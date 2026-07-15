n = int(input())


prime_numbers = []

# 0과 1은 소수가 아니므로 반드시 2부터 검사를 시작해야 합니다!
for num in range(2, n + 1):
    is_prime = True # 일단 num이 소수라고 가정합니다.
    
    # 2부터 자기 자신 바로 전(num - 1)까지의 수로 나누어 봅니다.
    for i in range(2, num):
        if num % i == 0:
            is_prime = False # 하나라도 나누어 떨어지면 소수가 아닙니다.
            break            # 소수가 아니므로 더 검사하지 않고 멈춥니다.
            
    if is_prime:
        prime_numbers.append(num)

# 리스트 앞에 *를 붙여 출력하면 대괄호 [ ] 없이 공백으로만 구분되어 출력됩니다.
print(*prime_numbers)