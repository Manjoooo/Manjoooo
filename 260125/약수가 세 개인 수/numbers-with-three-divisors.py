start, end = map(int, input().split())

# Please write your code here.
ans = 0
for i in range(start, end +1):
    divisor_cnt = 0
    for j in range(1,i+1):
        if i % j == 0:
            divisor_cnt += 1
    if divisor_cnt ==3:
        ans += 1
print(ans)

#첫번째 for문이 start와 end까지 돌면서 약수 개수를 세줌 
#특정 숫자 n의 약수의 개수를 알아내기 위해 1부터 n까지 해당 숫자를 나눠 나머지가 0인 개수를 세줌
#약수의 개수가 세개이면 정답 개수를 1증가 시켜줌 