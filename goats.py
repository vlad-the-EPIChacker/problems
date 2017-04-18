import sys

def cal(d1, d2):
    prob=0
    counter=0
    c2=0
    for i in range(0, len(d1)):
        n1=d1[i]
        for ii in range(0, len(d2)):
            n2=d2[ii]
            if n1>n2:
                prob=prob+1
            if n1==n2:
                c2=c2+1
            counter=counter+1
    counter=counter-c2
    prob=float(prob)/counter
    prob=round(prob, 5)
    print prob

f=open(sys.argv[1])
dice=f.readlines()
dice[0]=dice[0].split()
dice[1]=dice[1].split()
cal(dice[0], dice[1])