n = int(input())
current_char_code = ord('A')

for i in range(n):
    for j in range(i+1):
        print(chr(current_char_code), end="")
        current_char_code += 1
    
        if current_char_code > ord('Z'):
            current_char_code = ord('A')

    print()