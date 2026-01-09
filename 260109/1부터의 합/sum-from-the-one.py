n = int(input())
sumi = 0

for i in range(1,101):
    sumi += i
    if sumi >= n:
        print(i)
        break