f=open("clockpaperscissors.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    r=file[i].strip()
    p=0
    for ii in range(0, len(r)):
        if r[ii]=='1':
            p+=1
    if p>1:
        print 'Player 1'
    else:
        print 'Player 2'