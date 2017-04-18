import sys

def check(rows1, x, y):
    if y==l-1 and x==l:
        print 'Yes'
        sys.exit()
    if rows1[y][x]=='x':
        print 'No'
        return
    if rows1[y][x+1]=='x' and rows1[y+1][x]=='x':
        rows1[y][x]='x'
        check(rows1, 1, 0)
    if rows1[y][x+1]=='.':
        check(rows1, x+1, y)
    if rows1[y+1][x]=='.':
        check(rows1, x, y+1)

f=open(sys.argv[1])
file=f.readlines()
l=int(file[0])
rows=[]

for i in range(1, l+1):
    row=[]
    row.append('x')
    file[i]=list(file[i].rstrip())
    for ii in range(0, len(file[i])):
        row.append(file[i][ii])
    row.append('x')
    rows.append(row)
rowx=[]
for i in range(0, l+1):
    rowx.append('x')
rows.append(rowx)
check(rows, 1, 0)
