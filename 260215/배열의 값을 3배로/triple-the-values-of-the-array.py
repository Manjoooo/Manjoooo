arr = [list(map(int, input().split())) for _ in range(3)]
#공백을 쪼개서 정수를 리스트로 입력 받음. 
#for문은 한줄짜리 리스트를 세번 반복해서 만들라는 뜻. 

for i in range(3):
    for j in range(3):
        arr[i][j] *= 3

#일단 arr에서 값을 저장

for a in arr:
    for b in a:
        print(b, end= " ")
    print()
#첫번째 줄은 예: [1, 2, 3]을 먼저 꺼내고, 그다음 [4, 5, 6]을 꺼냅니다
#두번째 줄은 list 안에 있는 요소들을 출력합니다 즉 b가 element ex) 1