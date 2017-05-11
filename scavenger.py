
def run(rows, y, x, p):
    a=(0, 0)
    b=(0, 0)
    n = int(rows[y][x])

    if x==7 and y==7:
        return p+n, [(x, y)]
    if x+1<=7:
        a=run(rows, y, x+1, p+n)
    if y+1<=7:
        b=run(rows, y+1, x, p+n)
    if a[0]>b[0]:
        a[1].append((x, y))
        return a
    else:
        b[1].append((x, y))
        return b


f=open("scavenger.dat")
file=f.readlines()
rows=[file[i].split() for i in range(0, 8)]
jkl=run(rows, 0, 0, 0)
n=jkl[0]
coor=jkl[1][::-1]
for i in coor:
    rows[i[1]][i[0]]=' '
for i in rows:
    print ' '.join(i)
print "You collected", n, "points!"
