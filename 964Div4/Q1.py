testcases=int(input())
for i in range(testcases):
    num=int(input())
    sum=0
    while(num>0):
        digit=num%10
        sum=sum+digit
        num=num//10
    print(sum)