inp = input()
arr = inp.split()

a=int(arr[0])
b=int(arr[1])

#round 함수 사용하면 되묘!
c=(a+b) / (a-b)
print(f"{c:.2f}")