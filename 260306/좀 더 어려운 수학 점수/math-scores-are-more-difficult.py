# 첫째 줄 읽기 (80 90)
amat, aeng = map(int, input().split())
# 둘째 줄 읽기 (70 85)
bmat, beng = map(int, input().split())


if aeng != beng and amat >= bmat:
    print("A")
elif aeng != beng and bmat >= amat:
    print("B")
elif aeng >= beng and bmat == amat:
    print("A")
elif aeng <= beng and bmat == amat:
    print("B")


#데이터가 들어오는 줄 수에 맞춰서 입력을 각각 받았기 때문에