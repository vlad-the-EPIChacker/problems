import sys

def count(moo):
    x=0
    m=0
    while moo[x]=='M':
        m=m+1
        x=x+1
    y = x
    o = 0
    while y<len(moo):
        o = o + 1
        y = y + 1
    m=16*m
    final=chr(m+o)
    return final

f=open(sys.argv[1])
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    file[i]=file[i].rstrip()
    letters=file[i].split()
    final=''
    for ii in range(0, len(letters)):
        final=count(letters[ii])+final
    print final[::-1]