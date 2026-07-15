n = int(input())
current_char_code = ord('A')

for i in range(n):
    # 1. 행이 시작할 때 앞쪽 공백을 출력합니다.
    # 각 알파벳이 "알파벳 + 공백"으로 2칸씩 차지하므로, i * 2만큼 공백을 출력합니다.
    print(" " * (i * 2), end="")
    
    # 2. 알파벳을 출력하는 루프 (n - i개)
    for j in range(n - i):
        # 알파벳 뒤에 공백 " "을 하나 붙여서 출력합니다.
        print(chr(current_char_code), end=" ")
        current_char_code += 1
        
        # 'Z'를 넘어가면 'A'로 초기화
        if current_char_code > ord('Z'):
            current_char_code = ord('A')
            
    # 한 행 출력이 끝나면 줄바꿈
    print()