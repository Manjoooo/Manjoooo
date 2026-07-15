start, end = map(int, input().split())

# Please write your code here.
perfect_number_count = 0
# Please write your code here.
for num in range(start,end+1):
    cnt=0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    
    if cnt == 3:
        perfect_number_count += 1


print(perfect_number_count)