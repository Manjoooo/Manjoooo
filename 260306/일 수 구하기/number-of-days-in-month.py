# 변수 선언, 입력
n = int(input())


if n == 2:
	print("28")
elif n <= 7:
    if n % 2 == 1:
        print("31")
    else:
        print("30")
else:
    if n % 2 == 0:
        print("31")
    else:
        print("30")


# 일수,해당 월
#31일,"1월, 3월, 5월, 7월, 8월, 10월, 12월"
#30일,"4월, 6월, 9월, 11월"
#28일,2월
