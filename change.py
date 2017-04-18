import sys

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    n=int(file[i])
    coins=[[0, 47], [0, 37], [0, 23], [0, 13], [0, 5], [0, 1]]
    for ii in range(0, len(coins)):
        while (coins[ii][0]*coins[ii][1])<=n:
            if coins[ii][1]>n:
                break
            else:
                coins[ii][0]+=1
                n=n-coins[ii][1]
    print coins




