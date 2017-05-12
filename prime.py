def prime(n, k1, k2):
    primes=[]
    i=2
    while len(primes)<n:
        p=False
        for ii in range(2, i):
            if i%ii == 0:
                p=True
        if not p:
            if i>=k1 and i<=k2:
                primes.append(i**2)
            else:
                primes.append(i)
        i=i+1
    s=''
    for ii in primes:
        s=s+str(ii)+' '
    print s

f=open('prime.txt')
file=f.readlines()
nfile=int(file[0])

for i in range(1, nfile+1):
    line=file[i].strip()
    line=line.split()
    line=[int(line[i]) for i in range(0, len(line))]
    prime(line[0], line[1], line[2])
