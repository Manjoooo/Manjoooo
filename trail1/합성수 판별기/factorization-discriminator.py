n = int(input())
satisfied = False
    
for i in range(2, n):
    # n의 약수가 있다면 합성수입니다.
    if n % i == 0:
        satisfied = True

# 출력
if satisfied == True:
    print("C")
else:
    print("N")