import random
testcases=int(input())
for i in range(testcases):
    a1,a2,b1,b2 = map(int, input().split())
    wins=0

    for s1, s2 in [(a1, a2), (a2, a1)]:
        for sl1, sl2 in [(b1, b2), (b2, b1)]:
            p1 = 0
            p2 = 0

            if s1 > sl1:
                p1 += 1
            elif s1 < sl1:
                p2 += 1

            if s2 > sl2:
                p1 += 1
            elif s2 < sl2:
                p2 += 1
            
            if(p1>p2):
                wins+=1
    print(wins)


    # wins,win2=0,0
    # for rounds in range(3):
    #     ch1=random.choice([a1,a2])
    #     ch2=random.choice([b1,b2])
    #     if (ch1>ch2):
    #       wins+=1
    #     elif(ch1<ch2):
    #       win2+=1
    #     elif(ch1==ch2):
    #       break