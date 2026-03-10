inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

print(f"{a//b}.", end="")

# 일단 정수 부분을 먼저 출력 후 
#나눈 나머지에 10을 곱한 값을 b로 나눴을 떄의 몫을 순서대로 적는 것 계속 반복 

a %= b

for _ in range(20):
    a *= 10
    print(a//b, end="")


    a %= b

#그니까 for을 통해 뒤에 나머지 계산들을 이어서 붙이는 형식임