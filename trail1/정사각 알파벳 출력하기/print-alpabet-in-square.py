n = int(input())
current_char_code = ord('A')

for i in range(n):
    for j in range(n):
        print(chr(current_char_code), end="")
        current_char_code += 1
    print()