f=open("sammysays.dat")
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    line=file[i].strip()
    line=line.split()
    if line[0]=='Sammy' and line[1]=='says':
        c=line[2:]
        c=[c[ii]+' ' for ii in range(0, len(c))]
        c=''.join(c)
        print c