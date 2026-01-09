inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sumi = 0

for i in range(a,b+1):
    if i % 2 == 0:
        sumi += i

print(sumi)