n = int(input())
cnt = 1

for i in range(n):
    for j in range(i+1):
        print(cnt, end=" ")
        cnt += 1
    print()

#cnt가 누적되는 이유는 바깥에서 정의 
#i가 변하고 i의 숫자 range만큼 j의 값이 출력 그래서 삼각형으로 출력