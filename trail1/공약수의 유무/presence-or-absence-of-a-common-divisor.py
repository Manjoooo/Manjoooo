inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])

satisfied = False

# a부터 b까지 탐색 (b를 포함해야 하므로 b+1)
for i in range(a, b + 1):
    # i가 1920과 2880의 공약수(즉, 최대공약수 960의 약수)인지 확인
    if 960 % i == 0:
        satisfied = True
          # 하나라도 찾으면 더 볼 필요 없이 종료

if satisfied == True:
    print(1)
else:
    print(0)