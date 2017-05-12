def find(rows):
    for i in range(0, len(rows)):
        for ii in range(0, len(rows[i])):
            if rows[i][ii]=='S':
                return (i, ii)

def maze(rows, s):
    y=s[0]
    x=s[1]
    if rows[y][x]=='S':
        rows[y][x]='.'
    if rows[y][x]=='X':
        return True
    if rows[y][x]=='#' or rows[y][x]==' ':
        return False
    if rows[y][x]=='.':
        rows[y][x]=' '

    if maze(rows, (y+1, x)):
        return True

    if maze(rows, (y-1, x)):
        return True

    if maze(rows, (y, x+1)):
        return True

    if maze(rows, (y, x-1)):
        return True
    rows[y][x]='.'
    return False








f=open("maze.dat")
file=f.readlines()
nfile=int(file[0])
g=0
h=0
rows=[]

while g<nfile+1:
    if h>0 or file[h].strip()=='':
        row=list(file[h].strip())
        rows.append(row)

    if h%8==0:
        s=find(rows)
        g=g+1
        if h>0:
            maze(rows, s)
            rows[s[0]][s[1]]='S'
            for i in rows:
                print ''.join(i)
        rows=[]

    h=h+1

