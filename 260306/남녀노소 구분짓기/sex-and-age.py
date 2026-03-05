sex = int(input())
age = int(input())

if age >= 19:
    if sex == 0:
        print("MAN")
    else:
        print("WOMAN")
else:
    if sex == 0:
        print("BOY")
    else:
        print("GIRL")

# age, sex 입력 개인으로 입력 받기 한줄 한줄이니까 