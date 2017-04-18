f=open('chest.dat')
file=f.readlines()
nfile=int(file[0])
tran={}
tran['A']=0
tran['B']=1
tran['C']=2
tran['D']=3
tran['E']=4
tran['F']=5
tran['G']=6
tran['H']=7

for i in range(1, nfile+1):
    line=list(file[i].strip())
    x=tran[line[0]]
    y=8-int(line[1])
    rows=[['-','-','-','-','-','-','-','-',], ['-','-','-','-','-','-','-','-',], ['-','-','-','-','-','-','-','-',], ['-','-','-','-','-','-','-','-',], ['-','-','-','-','-','-','-','-',], ['-','-','-','-','-','-','-','-',], ['-','-','-','-','-','-','-','-',], ['-','-','-','-','-','-','-','-',]]
    rows[y][x]='K'
    if y+2<8 and y+2>0:
        if x+1<8 and x+1>0:
            rows[y+2][x+1]='?'
        if x-1<8 and x-1>0:
            rows[y+2][x-1]='?'
    if y-2<8 and y-2>0:
        if x+1<8 and x+1>0:
            rows[y-2][x+1]='?'
        if x-1<8 and x-1>0:
            rows[y-2][x-1]='?'
    if x+2<8 and x+2>0:
        if y+1<8 and y+1>0:
            rows[y+1][x+2]='?'
        if y-1<8 and y-1>0:
            rows[y-1][x+2]='?'
    if x-2<8 and x-2>0:
        if y+1<8 and y+1>0:
            rows[y+1][x-2]='?'
        if y-1<8 and y-1>0:
            rows[y-1][x-2]='?'

    for ii in range(0, 8):
        print ' '.join(rows[ii])
    print ''