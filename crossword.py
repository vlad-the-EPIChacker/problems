f=open('crosswordclues.dat')
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    words=file[i].strip()
    words=words.split()
    w1=words[0]
    w2=words[2]
    tf=False
    for ii in range(0, len(w1)):
        if not w2.find(w1[ii])==-1:
            tf=True
            w1y=w1.find(w1[ii])
            w2x=w2.find(w1[ii])
            break
    if tf==False:
        print 'none'
        print ''
        continue
    for iii in range(0, len(w2)):
        if iii==w2x:
            print w1
        else:
            m=w1y
            s=' '*m
            s=s+w2[iii]
            print s
    print ''